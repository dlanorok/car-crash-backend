from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from api.crashes.models import Crash
from api.crashes.serializers import CreateCrashSerializer, CrashSerializer


class CrashViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Crash.objects.all()
    serializer_class = CrashSerializer
    lookup_field = 'session_id'

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCrashSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Map to new serializer
        crash = self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(self.serializer_class(crash).data, status=status.HTTP_201_CREATED, headers=headers)
