from abc import abstractmethod

from api.common.helpers import get_session_id
from api.crashes.models import Crash


class SessionView:
    session_id = None

    def get_crash_id_from_headers(self):
        session_header = self.request.META.get('HTTP_X_SESSION', '').split()
        if session_header and len(session_header) > 1:
            return session_header[1]

    @abstractmethod
    def get_by_session(self, session_id):
        pass

    def get_queryset(self):
        self.session_id = get_session_id(self.request)
        return self.get_by_session(self.session_id)

    def get_crash_from_session(self):
        session_id = self.request.META.get('HTTP_X_SESSION', '').split()

        if session_id and len(session_id) > 1:
            return Crash.objects.get(session_id=session_id[1])
