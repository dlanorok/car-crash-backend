from django.dispatch import Signal
from rest_framework import mixins, viewsets

model_event = Signal(providing_args=['instance', 'sender_id'])

class EventView(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    def perform_create(self, serializer):
        instance = serializer.save()
        model_event.send(
            sender=self,
            instance=instance,
            sender_id=self.request.session.session_key,
            event_type='model_create'
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        model_event.send(
            sender=self,
            instance=instance,
            sender_id=self.request.session.session_key,
            event_type='model_update'
        )

