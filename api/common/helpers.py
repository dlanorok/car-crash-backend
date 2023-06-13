def get_session_id(request):
    session_id = request.META.get('HTTP_X_SESSION', '').split()

    if session_id and len(session_id) > 1:
        return session_id[1]

    return None
