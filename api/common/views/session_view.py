from abc import abstractmethod

from api.common.helpers import get_session_id
from api.crashes.models import Crash


class SessionView:
    @abstractmethod
    def get_by_session(self, session_id):
        pass

    def get_queryset(self):
        session_id = get_session_id(self.request)

        if session_id:
            return self.get_by_session(session_id)

        return []

    def get_crash_from_session(self):
        session_id = self.request.META.get('HTTP_X_SESSION', '').split()

        if session_id and len(session_id) > 1:
            return Crash.objects.get(session_id=session_id[1])
