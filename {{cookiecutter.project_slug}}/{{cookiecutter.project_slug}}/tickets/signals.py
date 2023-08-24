from django.core.cache import cache
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from {{ cookiecutter.project_slug }}.tickets.models import Ticket


@receiver(post_save, sender=Ticket)
def ticket_to_cache(sender, instance: Ticket, created, **kwargs):
    if created:
        cache.set_many(
            {
                f"{instance.id}": True,
                f"{instance.id}-current": 0,
                f"{instance.id}-name": instance.name,
                f"{instance.id}-max": instance.max,
                f"{instance.id}-next": instance.next,
            },
            3600,
        )


@receiver(pre_save, sender=Ticket)
def update_ticket(sender, instance: Ticket, **kwargs):
    if instance.id is not None:
        cache.set_many(
            {
                f"{instance.id}": True,
                f"{instance.id}-name": instance.name,
                f"{instance.id}-max": instance.max,
                f"{instance.id}-next": instance.next,
            },
            3600,
        )


@receiver(post_delete, sender=Ticket)
def delete_ticket(sender, instance: Ticket, **kwargs):
    uuid = instance.id
    cache.delete_many(
        [f"{uuid}", f"{uuid}-max", f"{uuid}-current", f"{uuid}-name", f"{uuid}-next"]
    )
