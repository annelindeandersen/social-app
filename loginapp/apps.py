from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class LoginappConfig(AppConfig):
    name = 'loginapp'

    def ready(self):
        import loginapp.signals