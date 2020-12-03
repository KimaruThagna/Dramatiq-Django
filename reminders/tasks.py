import arrow
import dramatiq

from django.conf import settings

from .models import Appointment



@dramatiq.actor
def send_sms_reminder(appointment_id):

    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = f'Hi {appointment.name}. You have an appointment coming up at {appointment.time.format("h:mm a")}.'
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(body)

def send_sms_from_apscheduler(appointment_id):

    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = f'Hi {appointment.name}. You have an appointment coming up at {appointment.time.format("h:mm a")}.'
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(body)
