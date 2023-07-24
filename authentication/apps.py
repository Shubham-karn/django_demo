# authentication/apps.py

from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    name = 'authentication'

    # Add this method to import the admin.py file
    def ready(self):
        import authentication.admin
