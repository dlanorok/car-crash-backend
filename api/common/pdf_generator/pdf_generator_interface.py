from api.crashes.models import Crash


class PdfGeneratorInterface:
    crash: Crash

    def __init__(self, crash):
        self.crash = crash

    def prepare_pdf(self):
        pass

    def write(self):
        pass
