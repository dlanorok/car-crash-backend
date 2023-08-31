from api.common.pdf_generator.py_pdf_generator import PyPdfGenerator


def create_pdf_from_crash(crash):
    pdf_generator = PyPdfGenerator(crash)
    pdf_generator.prepare_pdf()
    pdf_generator.write()
