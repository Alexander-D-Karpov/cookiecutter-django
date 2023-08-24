{%- if cookiecutter.ticket_app == 'y' %}from django.urls import include, path{%- endif %}

app_name = "api"
urlpatterns = [
{%- if cookiecutter.ticket_app == 'y' %}
    path("ticket/", include("{{ cookiecutter.project_slug }}.tickets.api.urls")),
{%- endif %}
]
