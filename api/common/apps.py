from django.apps import AppConfig
from django.core.signals import setting_changed



class CommonConfig(AppConfig):
    name = 'api.common'

    def ready(self):
        from api.common.signals import send_model_event
        setting_changed.connect(send_model_event)
