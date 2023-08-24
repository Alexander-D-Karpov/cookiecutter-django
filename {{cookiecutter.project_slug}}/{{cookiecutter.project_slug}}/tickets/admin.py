from django.contrib import admin

from {{ cookiecutter.project_slug }}.tickets.models import Ticket

admin.site.register(Ticket)
