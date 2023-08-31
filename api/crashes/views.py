from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.common.pdf_generator.py_pdf_generator import PyPdfGenerator
from api.common.views.event_view import EventView
from api.crashes.models import Crash
from api.crashes.serializers import CrashSerializer


class CrashViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   EventView):
    queryset = Crash.objects.all()
    serializer_class = CrashSerializer
    lookup_field = 'session_id'

    def perform_create(self, serializer):
        # Create session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer.validated_data['creator'] = self.request.session.session_key

        super().perform_create(serializer)

    @action(detail=True, methods=['post'])
    def generate_pdf(self, request, session_id=None):
        crash = self.get_object()
        pdf_generator = PyPdfGenerator(crash)
        pdf_generator.prepare_pdf()
        pdf_generator.write()

        return Response(status=status.HTTP_204_NO_CONTENT)
