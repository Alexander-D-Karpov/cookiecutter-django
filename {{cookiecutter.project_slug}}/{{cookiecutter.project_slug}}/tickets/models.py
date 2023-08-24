import uuid

from django.db import models
from django.urls import reverse


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, default="processing...")
    max = models.IntegerField(default=0)
    next = models.URLField(null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    def get_absolute_url(self):
        return reverse("api:ticket", kwargs={"uuid": self.id})
