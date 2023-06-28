from rest_framework import mixins
from rest_framework.response import Response

from api.cars.models import Car
from api.common.views.event_view import EventView, model_event
from api.crashes.models import Crash
from api.crashes.serializers import CrashSerializer
from api.sketches.models import Sketch


class CrashViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   EventView):
    queryset = Crash.objects.all()
    serializer_class = CrashSerializer
    lookup_field = 'session_id'

    def retrieve(self, request, *args, **kwargs):
        crash = self.get_object()

        create_car = True

        # Check session
        if self.request.session.exists(self.request.session.session_key):
            if Car.objects.filter(creator=self.request.session.session_key, crash__session_id=crash.session_id).count() == 0:
                create_car = True
            else:
                create_car = False

        # Create session
        if create_car:
            self.request.session.create()
            car = Car(crash=crash, creator=self.request.session.session_key)
            car.save()
            model_event.send(
                sender=self,
                instance=car,
                sender_id=self.request.session.session_key,
                event_type='model_create'
            )

        serializer = self.get_serializer(crash)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Create session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer.validated_data['creator'] = self.request.session.session_key

        instance = super().perform_create(serializer)

        Sketch(creator=self.request.session.session_key, crash=instance).save()
