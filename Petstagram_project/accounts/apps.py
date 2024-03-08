from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Petstagram_project.accounts'

    def ready(self):
        import Petstagram_project.accounts.signals

