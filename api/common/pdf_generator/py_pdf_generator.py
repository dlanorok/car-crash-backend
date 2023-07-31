import io

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

from api.cars.models import Car
from api.common.pdf_generator.pdf_generator_interface import PdfGeneratorInterface
from api.common.pdf_generator.statement_enum import AccidentStatementEnums
from api.crashes.models import Crash


class PyPdfGenerator(PdfGeneratorInterface):
    def __init__(self, crash: Crash):
        super().__init__(crash)

        reader = PdfReader("assets/statement_si.pdf")
        self.writer = PdfWriter()
        page = reader.pages[0]

        packet = io.BytesIO()
        image_path = 'assets/img.png'
        can = Canvas(packet, pagesize=letter)
        x = 125
        y = 75
        width = 335
        height = 170
        can.drawImage(image_path, x, y, width, height)
        can.save()
        packet.seek(0)
        modified_page = PdfReader(packet)
        modified_page = modified_page.pages[0]
        page.merge_page(modified_page)

        self.writer.add_page(page)

    def prepare_pdf(self):
        car: Car = self.crash.cars.first()

        write_fields = {
            AccidentStatementEnums.DATE_OF_ACCIDENT: self.crash.date_of_accident,
            AccidentStatementEnums.TIME_OF_ACCIDENT: self.crash.date_of_accident,
            AccidentStatementEnums.ACCIDENT_COUNTRY: self.crash.country,
            AccidentStatementEnums.ACCIDENT_PLACE: self.crash.place,
            AccidentStatementEnums.INJURIES_NO: 'TODO',
            AccidentStatementEnums.INJURIES_YES: 'TODO',
            AccidentStatementEnums.VEHICLE_MATERIAL_DAMAGE_NO: 'TODO',
            AccidentStatementEnums.VEHICLE_MATERIAL_DAMAGE_YES: 'TODO',
            AccidentStatementEnums.OTHER_MATERIAL_DAMAGE_NO: 'TODO',
            AccidentStatementEnums.OTHER_MATERIAL_DAMAGE_YES: 'TODO',
            AccidentStatementEnums.WITNESSES: 'TODO',
        }

        if car:
            write_fields.update({
                AccidentStatementEnums.CAR_TYPE: car.car_type,
                AccidentStatementEnums.CAR_REGISTRATION_PLATE: car.registration_plate,
                AccidentStatementEnums.CAR_REGISTRATION_COUNTRY: car.registration_country
            })

            if getattr(car, 'policy_holder', None):
                write_fields.update({
                    AccidentStatementEnums.POLICY_HOLDER_NAME: car.policy_holder.name,
                    AccidentStatementEnums.POLICY_HOLDER_ADDRESS: car.policy_holder.address,
                    AccidentStatementEnums.POLICY_HOLDER_EMAIL: car.policy_holder.email,
                    AccidentStatementEnums.POLICY_HOLDER_POST_NUMBER: car.policy_holder.post_number,
                    AccidentStatementEnums.POLICY_HOLDER_COUNTRY: car.policy_holder.country_code,
                })

            if getattr(car, 'insurance', None):
                write_fields.update({
                    AccidentStatementEnums.INSURANCE_NAME: car.insurance.name,
                    AccidentStatementEnums.INSURANCE_POLICY_NUMBER: car.insurance.policy_number,
                    AccidentStatementEnums.INSURANCE_GREEN_CARD: car.insurance.green_card,
                    AccidentStatementEnums.INSURANCE_VALID_UNTIL: car.insurance.valid_until,
                    AccidentStatementEnums.INSURANCE_DAMAGED_INSURED_NO: 'todo',
                    AccidentStatementEnums.INSURANCE_DAMAGED_INSURED_YES: 'todo',
                })

            if getattr(car, 'driver', None):
                write_fields.update({
                    AccidentStatementEnums.DRIVER_SURNAME: car.driver.surname,
                    AccidentStatementEnums.DRIVER_NAME: car.driver.name,
                    AccidentStatementEnums.DRIVER_BIRTHDAY: car.driver.birthday,
                    AccidentStatementEnums.DRIVER_ADDRESS: car.driver.address,
                    AccidentStatementEnums.DRIVER_EMAIL: car.driver.email,
                    AccidentStatementEnums.DRIVER_COUNTRY: car.driver.country,
                    AccidentStatementEnums.DRIVER_LICENSE_NUMBER: car.driver.driving_licence_number,
                    AccidentStatementEnums.DRIVER_LICENSE_VALID_TO: car.driver.driving_licence_valid_to
                })


        self.writer.update_page_form_field_values(
            self.writer.pages[0], write_fields
        )


    def write(self):
        with open("filled-out.pdf", "wb") as output_stream:
            self.writer.write(output_stream)
