# {{cookiecutter.project_name}}

{{ cookiecutter.description }}
## Basic Commands

### Runserver

    $ ./manage.py runserver_plus

### Type checks

Running type checks with mypy:

    $ mypy {{cookiecutter.project_slug}}

#### Running tests with pytest

    $ pytest

### Setting Up Your Users

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

{%- if cookiecutter.use_celery == "y" %}

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd {{cookiecutter.project_slug}}
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

{%- endif %}
{%- if cookiecutter.use_sentry == "y" %}

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
{%- endif %}


made with [cookiecutter-django](https://github.com/Alexander-D-Karpov/cookiecutter-django)
