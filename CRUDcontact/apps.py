from django.apps import AppConfig


class CrudcontactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CRUDcontact'

    def ready(self):
        import CRUDcontact.signals