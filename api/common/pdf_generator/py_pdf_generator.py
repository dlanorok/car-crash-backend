import io
from datetime import datetime

import fitz
from PIL import Image
from django.core.files import File as CoreFile
from django.core.files.storage import default_storage
from django.db.models import BooleanField
from django.dispatch import Signal
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

from api.common.pdf_generator.pdf_generator_interface import PdfGeneratorInterface
from api.common.pdf_generator.si_field_mapper import field_mapper
from api.common.pdf_generator.statement_enum import AccidentStatementEnums
from api.crashes.models import Crash
from api.files.models import File
from config import settings

pdf_generator_event = Signal(providing_args=['instance', 'sender_id'])


class PyPdfGenerator(PdfGeneratorInterface):
    def __init__(self, crash: Crash):
        super().__init__(crash)

        self.questionnaires = self.crash.questionnaires.all()
        self.doc = fitz.open('assets/accident_report.pdf')
        self.page = self.doc[0]

        self.draw_sketch()
        self.draw_initial_impact()
        self.draw_damaged_parts()

    def draw_damaged_parts(self):
        for index, questionnaire in enumerate(self.questionnaires):
            car = questionnaire.car
            if index > 1 or not car.damaged_parts_svg_file:
                continue

            y = self.page.mediabox.height - 75
            width = 30
            x = 50
            if index == 1:
                x = self.page.mediabox.width - 90

            try:
                s3_file = default_storage.open(car.damaged_parts_svg_file.file.name)
                svg_content = s3_file.read()
                drawing = svg2rlg(io.BytesIO(svg_content))
                pdfbytes = renderPDF.drawToString(drawing)
                pix_doc = fitz.open("pdf", pdfbytes)
                self.doc[0].insert_image(fitz.Rect(x, y - width, x + width, y),
                                  pixmap=pix_doc.get_page_pixmap(0))
            except:
                return

    def draw_initial_impact(self):
        for index, questionnaire in enumerate(self.questionnaires):
            car = questionnaire.car
            if index > 1 or not car.initial_impact_svg_file:
                continue

            y = self.page.mediabox.height - 135
            width = 70
            x = 40
            if index == 1:
                x = self.page.mediabox.width - 110

            try:
                s3_file = default_storage.open(car.initial_impact_svg_file.file.name)
                svg_content = s3_file.read()
                drawing = svg2rlg(io.BytesIO(svg_content))
                pdfbytes = renderPDF.drawToString(drawing)
                pix_doc = fitz.open("pdf", pdfbytes)
                self.doc[0].insert_image(fitz.Rect(x, y - width, x + width, y),
                                  pixmap=pix_doc.get_page_pixmap(0))
            except:
                return



    def draw_sketch(self):
        if not self.crash.sketch or not self.crash.sketch.file:
            return

        try:
            s3_file = default_storage.open(self.crash.sketch.file.file.name)
            image = s3_file.read()
            img = Image.open(io.BytesIO(image))
        except:
            return

        # define position of img
        x = 128
        y = self.page.mediabox.height - 73
        img_width, img_height = img.size
        max_width = 340
        max_height = 170

        rect_aspect_ratio = max_width / max_height
        img_aspect_ratio = img_width / img_height
        crop_x = 0
        crop_y = 0
        crop_width = img_width
        crop_height = img_height

        if img_aspect_ratio > rect_aspect_ratio:
            # Image is wider than the rectangle
            # Crop the width to fit the rectangle's width
            crop_width = int(max_width * (img_height / max_height))
            crop_x = int((img_width - crop_width) / 2)
        else:
            # Image is taller than the rectangle
            # Crop the height to fit the rectangle's height
            crop_height = int(max_height * (img_width / max_width))
            crop_y = int((img_height - crop_height) / 2)

        img = img.crop((crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))

        # draw image
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        self.page.insert_image(fitz.Rect(x, y - max_height, x + max_width, y),  stream=imgByteArr)


    def prepare_pdf(self):
        witness_merged_data = ''
        write_fields = {
            AccidentStatementEnums.DATE_OF_ACCIDENT: self.crash.date_of_accident.strftime("%d.%m.%Y"),
            AccidentStatementEnums.TIME_OF_ACCIDENT: self.crash.date_of_accident.strftime("%H:%M"),
            AccidentStatementEnums.ACCIDENT_COUNTRY: str(self.crash.country),
            AccidentStatementEnums.ACCIDENT_PLACE_1: self.crash.place[0:28],
            AccidentStatementEnums.ACCIDENT_PLACE_2: self.crash.place[28:],
            AccidentStatementEnums.INJURIES_YES: self.crash.injuries,
            AccidentStatementEnums.INJURIES_NO: not self.crash.injuries,
            AccidentStatementEnums.OTHER_MATERIAL_DAMAGE_YES: self.crash.other_material_damage,
            AccidentStatementEnums.OTHER_MATERIAL_DAMAGE_NO: not self.crash.other_material_damage,
            AccidentStatementEnums.VEHICLE_MATERIAL_DAMAGE_YES: self.crash.vehicle_material_damage,
            AccidentStatementEnums.VEHICLE_MATERIAL_DAMAGE_NO: not self.crash.vehicle_material_damage,
        }

        for i, car in enumerate(self.crash.cars.all()):
            witness_merged_data += car.witnesses + "\n"

            circumstance_count = 0
            for field in car.circumstances._meta.fields:
                if field.__class__ is BooleanField:
                    if getattr(car.circumstances, field.attname):
                        circumstance_count += 1


            write_fields.update({
                f'{AccidentStatementEnums.CIRCUMSTANCES_COUNT}_{i + 1}': str(circumstance_count),

                f'{AccidentStatementEnums.POLICY_HOLDER_SURNAME}_{i+1}': car.policy_holder.surname,
                f'{AccidentStatementEnums.POLICY_HOLDER_NAME}_{i+1}': car.policy_holder.name,
                f'{AccidentStatementEnums.POLICY_HOLDER_EMAIL}_{i+1}': car.policy_holder.email_phone_number,
                f'{AccidentStatementEnums.POLICY_HOLDER_ADDRESS}_{i+1}': car.policy_holder.address,
                f'{AccidentStatementEnums.POLICY_HOLDER_COUNTRY}_{i+1}': car.policy_holder.country_code,

                f'{AccidentStatementEnums.CAR_TYPE}_{i + 1}': car.car_type,
                f'{AccidentStatementEnums.CAR_REGISTRATION_PLATE}_{i + 1}': car.registration_plate,
                f'{AccidentStatementEnums.CAR_REGISTRATION_COUNTRY}_{i + 1}': car.registration_country,
                f'{AccidentStatementEnums.ADDITIONAL_DATA}_{i + 1}': car.additional_data,

                f'{AccidentStatementEnums.INSURANCE_NAME}_{i + 1}': car.insurance.name,
                f'{AccidentStatementEnums.INSURANCE_POLICY_NUMBER}_{i + 1}': car.insurance.policy_number,
                f'{AccidentStatementEnums.INSURANCE_GREEN_CARD}_{i + 1}': car.insurance.green_card,
                f'{AccidentStatementEnums.INSURANCE_AGENCY_ADDRESS}_{i + 1}': car.insurance.address,
                f'{AccidentStatementEnums.INSURANCE_VALID_FROM}_{i + 1}': car.insurance.valid_from.strftime("%d.%m.%Y") if car.insurance.valid_from else '',
                f'{AccidentStatementEnums.INSURANCE_VALID_UNTIL}_{i + 1}': car.insurance.valid_until.strftime("%d.%m.%Y") if car.insurance.valid_until else '' ,
                f'{AccidentStatementEnums.INSURANCE_AGENCY}_{i + 1}': car.insurance.agent,
                f'{AccidentStatementEnums.CAR_CASCO_YES}_{i + 1}': car.insurance.damage_insured,
                f'{AccidentStatementEnums.CAR_CASCO_NO}_{i + 1}': not car.insurance.damage_insured,

                f'{AccidentStatementEnums.DRIVER_SURNAME}_{i + 1}': car.driver.surname,
                f'{AccidentStatementEnums.DRIVER_NAME}_{i + 1}': car.driver.name,
                f'{AccidentStatementEnums.DRIVER_BIRTHDAY}_{i + 1}': car.driver.date_of_birth.strftime("%d.%m.%Y") if car.driver.date_of_birth else '',
                f'{AccidentStatementEnums.DRIVER_ADDRESS}_{i + 1}': car.driver.address,
                f'{AccidentStatementEnums.DRIVER_COUNTRY}_{i + 1}': car.driver.country,
                f'{AccidentStatementEnums.DRIVER_EMAIL}_{i + 1}': car.driver.email or car.driver.phone_number,
                f'{AccidentStatementEnums.DRIVER_LICENSE_NUMBER}_{i + 1}': car.driver.driving_licence_number,
                f'{AccidentStatementEnums.DRIVER_LICENSE_CATEGORY}_{i + 1}': car.driver.driving_licence_category,
                f'{AccidentStatementEnums.DRIVER_LICENSE_VALID_TO}_{i + 1}': car.driver.driving_licence_valid_to.strftime("%d.%m.%Y") if car.driver.driving_licence_valid_to else '',

                f'{AccidentStatementEnums.PARKED_STOPPED}_{i + 1}': car.circumstances.parked_stopped,
                f'{AccidentStatementEnums.LEAVING_PARKING_OPENING_DOOR}_{i + 1}': car.circumstances.leaving_parking_opening_door,
                f'{AccidentStatementEnums.ENTERING_PARKING}_{i + 1}': car.circumstances.entering_parking,
                f'{AccidentStatementEnums.EMERGING_FROM_CAR_PARK}_{i + 1}': car.circumstances.emerging_from_car_park,
                f'{AccidentStatementEnums.ENTERING_CAR_PARK}_{i + 1}': car.circumstances.entering_car_park,
                f'{AccidentStatementEnums.ENTERING_ROUNDABOUT}_{i + 1}': car.circumstances.entering_roundabout,
                f'{AccidentStatementEnums.CIRCULATING_ROUNDABOUT}_{i + 1}': car.circumstances.circulating_roundabout,
                f'{AccidentStatementEnums.REAR_SAME_DIRECTION}_{i + 1}': car.circumstances.rear_same_direction,
                f'{AccidentStatementEnums.SAME_DIRECTION_DIFFERENT_LANE}_{i + 1}': car.circumstances.same_direction_different_lane,
                f'{AccidentStatementEnums.CHANGING_LANES}_{i + 1}': car.circumstances.changing_lanes,
                f'{AccidentStatementEnums.OVERTAKING}_{i + 1}': car.circumstances.overtaking,
                f'{AccidentStatementEnums.TURNING_RIGHT}_{i + 1}': car.circumstances.turning_right,
                f'{AccidentStatementEnums.TURNING_LEFT}_{i + 1}': car.circumstances.turning_left,
                f'{AccidentStatementEnums.REVERSING}_{i + 1}': car.circumstances.reversing,
                f'{AccidentStatementEnums.DRIVING_ON_OPPOSITE_LANE}_{i + 1}': car.circumstances.driving_on_opposite_lane,
                f'{AccidentStatementEnums.FROM_RIGHT_CROSSING}_{i + 1}': car.circumstances.from_right_crossing,
                f'{AccidentStatementEnums.DISREGARDING_RIGHT_OF_WAY_RED_LIGHT}_{i + 1}': car.circumstances.disregarding_right_of_way_red_light,

                f'{AccidentStatementEnums.SIGNATURE}_{i + 1}': f'{car.driver.name}\n{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}',
            })

        write_fields.update({
            f'{AccidentStatementEnums.WITNESSES}': witness_merged_data,
        })

        for page in self.doc:
            widgets = page.widgets()
            for widget in widgets:
                if widget.field_name in field_mapper:
                    mapper = field_mapper.get(widget.field_name)

                    if not mapper:
                        continue

                    value = write_fields.get(mapper.get("name")) or ''
                    widget.field_value = value
                    widget.text_fontsize = 0
                    widget.update()


    def write(self):
        output_buffer = io.BytesIO()
        self.doc.save(output_buffer)
        output_buffer.seek(0)
        self.doc.close()

        if not self.crash.pdf:
            self.crash.pdf = File(file=CoreFile(output_buffer, name=f'{self.crash.id}_{settings.ENV}.pdf'), file_name=f'{self.crash.id}_{settings.ENV}.pdf')
        else:
            self.crash.pdf.file.delete()
            self.crash.pdf.file.save(f'{self.crash.id}_{settings.ENV}.pdf', output_buffer)

        self.crash.pdf.save()
        self.crash.save()
        output_buffer.close()

        pdf_generator_event.send(
            sender=None,
            instance=self.crash,
            sender_id='',
            event_type='model_update'
        )
