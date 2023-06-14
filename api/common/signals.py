from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver

from api.circumstances.serializers import CircumstanceSerializer
from api.common.views.event_view import model_event
from api.crashes.serializers import CrashSerializer
from api.drivers.serializers import DriverSerializer
from api.insurances.serializers import InsuranceSerializer
from api.policy_holders.serializers import PolicyHolderSerializer

car_serializers = {
    'PolicyHolder': PolicyHolderSerializer,
    'Driver': DriverSerializer,
    'Insurance': InsuranceSerializer,
    'Circumstance': CircumstanceSerializer
}


@receiver(model_event)
def send_model_event(sender, instance, **kwargs):
    model_name = instance._meta.model.__name__
    type = kwargs['event_type']

    if model_name in car_serializers:
        _send_model_update(
            instance.car.crash.session_id,
            car_serializers[model_name](instance).data,
            kwargs['sender_id'],
            model_name,
            type
        )
    elif model_name == 'Car':
        _send_model_update(
            instance.crash.session_id,
            CrashSerializer(instance).data,
            kwargs['sender_id'],
            model_name,
            type
        )
    elif model_name == 'Crash':
        _send_model_update(
            instance.session_id,
            CrashSerializer(instance).data,
            kwargs['sender_id'],
            model_name,
            type
        )


def _send_model_update(crash_session_id, data, sender_id, model_name, type):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'crash_{crash_session_id}',
        {
            "type": type,
            'sender_id': sender_id,
            "model_name": model_name,
            "model": data
        }
    )
