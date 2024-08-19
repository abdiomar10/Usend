from django.apps import AppConfig


class UsendappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UsendApp'

    def ready(self):
        import UsendApp.signals


