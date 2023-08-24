from django.apps import AppConfig


class TicketsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.project_slug }}.tickets"

    def ready(self):
        try:
            import {{ cookiecutter.project_slug }}.tickets.signals  # noqa F401
        except ImportError:
            pass
