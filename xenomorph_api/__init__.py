from django.apps import AppConfig


class MyAppConfig(AppConfig):
    # ...

    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        default_app_config = 'apps.MyAppConfig'
