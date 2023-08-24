from django.urls import path

from {{ cookiecutter.project_slug }}.tickets.api.views import RetrieveTicketSerializer

urlpatterns = [
    path("<str:uuid>", RetrieveTicketSerializer.as_view(), name="ticket"),
]
