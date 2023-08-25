from rest_framework import viewsets, mixins

from api.files.models import File
from api.files.serializers import FileSerializer


class FileViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
