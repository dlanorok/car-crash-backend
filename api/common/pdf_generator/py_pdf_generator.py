import io
import os

from PyPDF2 import PdfReader, PdfWriter
from django.core.files import File as CoreFile
from django.dispatch import Signal
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from svglib.svglib import svg2rlg

from api.common.pdf_generator.pdf_generator_interface import PdfGeneratorInterface
from api.crashes.models import Crash
from api.files.models import File

pdf_generator_event = Signal(providing_args=['instance', 'sender_id'])


class PyPdfGenerator(PdfGeneratorInterface):
    def __init__(self, crash: Crash):
        super().__init__(crash)

        reader = PdfReader("assets/statement_si.pdf")
        self.writer = PdfWriter()
        self.page = reader.pages[0]
        self.questionnaires = self.crash.questionnaires.all()

        packet = io.BytesIO()
        canvas = Canvas(packet, pagesize=letter)
        canvas.setFillColorRGB(1,1,1)

        self.draw_sketch(canvas)
        self.draw_initial_impact(canvas)
        self.draw_damaged_parts(canvas)
        canvas.save()

        packet.seek(0)
        modified_page = PdfReader(packet)
        modified_page = modified_page.pages[0]
        self.page.merge_page(modified_page)

        self.writer.add_page(self.page)

    def draw_damaged_parts(self, canvas):
        for index, questionnaire in enumerate(self.questionnaires):
            car = questionnaire.car
            if index > 1 or not car.damaged_parts_svg_file:
                continue

            rect_x = 25
            rect_width = 95
            drawing_x = 50
            y = 80

            if index == 1:
                width = int(self.page.mediabox.width)
                rect_x = width - 30 - rect_width
                drawing_x = width - 100

            canvas.rect(rect_x, y, rect_width, 30, fill=1, stroke=0)
            drawing = svg2rlg(car.damaged_parts_svg_file.file.path)

            drawing.scale(0.1, 0.1)

            # draw image
            renderPDF.draw(drawing, canvas, drawing_x, y)

    def draw_initial_impact(self, canvas):
        for index, questionnaire in enumerate(self.questionnaires):
            car = questionnaire.car
            if index > 1 or not car.initial_impact_svg_file:
                continue

            rect_x = 25
            rect_width = 95
            drawing_x = 50
            y = 135
            if index == 1:
                width = int(self.page.mediabox.width)
                rect_x = width - 30 - rect_width
                drawing_x = width - 100

            canvas.rect(rect_x, y, rect_width, 75, fill=1, stroke=0)
            drawing = svg2rlg(car.initial_impact_svg_file.file.path)

            drawing.scale(0.16, 0.16)

            # draw image
            renderPDF.draw(drawing, canvas, drawing_x, y)

    def draw_sketch(self, canvas):
        if not self.crash.sketch or not self.crash.sketch.file:
            return

        img = ImageReader(self.crash.sketch.file.file.path)

        # define position of img
        x = 125
        y = 75
        width = 335
        height = 170

        # draw image
        canvas.drawImage(img, x, y, width, height, preserveAspectRatio=True)


    def prepare_pdf(self):
        pass
        # car: Car = self.crash.cars.first()
        #
        # write_fields = {
        #     AccidentStatementEnums.DATE_OF_ACCIDENT: self.crash.date_of_accident,
        #     AccidentStatementEnums.TIME_OF_ACCIDENT: self.crash.date_of_accident,
        #     AccidentStatementEnums.ACCIDENT_COUNTRY: self.crash.country,
        #     AccidentStatementEnums.ACCIDENT_PLACE: self.crash.place,
        #     AccidentStatementEnums.INJURIES_NO: 'TODO',
        #     AccidentStatementEnums.INJURIES_YES: 'TODO',
        #     AccidentStatementEnums.VEHICLE_MATERIAL_DAMAGE_NO: 'TODO',
        #     AccidentStatementEnums.VEHICLE_MATERIAL_DAMAGE_YES: 'TODO',
        #     AccidentStatementEnums.OTHER_MATERIAL_DAMAGE_NO: 'TODO',
        #     AccidentStatementEnums.OTHER_MATERIAL_DAMAGE_YES: 'TODO',
        #     AccidentStatementEnums.WITNESSES: 'TODO',
        # }
        #
        # if car:
        #     write_fields.update({
        #         AccidentStatementEnums.CAR_TYPE: car.car_type,
        #         AccidentStatementEnums.CAR_REGISTRATION_PLATE: car.registration_plate,
        #         AccidentStatementEnums.CAR_REGISTRATION_COUNTRY: car.registration_country
        #     })
        #
        #     if getattr(car, 'policy_holder', None):
        #         write_fields.update({
        #             AccidentStatementEnums.POLICY_HOLDER_NAME: car.policy_holder.name,
        #             AccidentStatementEnums.POLICY_HOLDER_ADDRESS: car.policy_holder.address,
        #             AccidentStatementEnums.POLICY_HOLDER_EMAIL: car.policy_holder.email,
        #             AccidentStatementEnums.POLICY_HOLDER_POST_NUMBER: car.policy_holder.post_number,
        #             AccidentStatementEnums.POLICY_HOLDER_COUNTRY: car.policy_holder.country_code,
        #         })
        #
        #     if getattr(car, 'insurance', None):
        #         write_fields.update({
        #             AccidentStatementEnums.INSURANCE_NAME: car.insurance.name,
        #             AccidentStatementEnums.INSURANCE_POLICY_NUMBER: car.insurance.policy_number,
        #             AccidentStatementEnums.INSURANCE_GREEN_CARD: car.insurance.green_card,
        #             AccidentStatementEnums.INSURANCE_VALID_UNTIL: car.insurance.valid_until,
        #             AccidentStatementEnums.INSURANCE_DAMAGED_INSURED_NO: 'todo',
        #             AccidentStatementEnums.INSURANCE_DAMAGED_INSURED_YES: 'todo',
        #         })
        #
        #     if getattr(car, 'driver', None):
        #         write_fields.update({
        #             AccidentStatementEnums.DRIVER_SURNAME: car.driver.surname,
        #             AccidentStatementEnums.DRIVER_NAME: car.driver.name,
        #             AccidentStatementEnums.DRIVER_BIRTHDAY: car.driver.birthday,
        #             AccidentStatementEnums.DRIVER_ADDRESS: car.driver.address,
        #             AccidentStatementEnums.DRIVER_EMAIL: car.driver.email,
        #             AccidentStatementEnums.DRIVER_COUNTRY: car.driver.country,
        #             AccidentStatementEnums.DRIVER_LICENSE_NUMBER: car.driver.driving_licence_number,
        #             AccidentStatementEnums.DRIVER_LICENSE_VALID_TO: car.driver.driving_licence_valid_to
        #         })
        #
        #
        # self.writer.update_page_form_field_values(
        #     self.writer.pages[0], write_fields
        # )


    def write(self):
        output_buffer = io.BytesIO()
        self.writer.write(output_buffer)
        output_buffer.seek(0)
        if self.crash.pdf:
            try:
                os.remove(self.crash.pdf.file.path)
                self.crash.pdf.delete()
            except:
                print('File does not exists')

        pdf = File(file=CoreFile(output_buffer, name=f'{self.crash.id}.pdf'), name=f'{self.crash.id}.pdf')
        pdf.save()
        self.crash.pdf = pdf
        self.crash.save()
        output_buffer.close()

        pdf_generator_event.send(
            sender=None,
            instance=self.crash,
            sender_id='',
            event_type='model_update'
        )
