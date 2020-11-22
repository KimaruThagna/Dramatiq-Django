from django.db import models
from timezone_field import TimeZoneField
from django.shortcuts import reverse
import arrow

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='UTC')

    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Appointment #{self.pk} - {self.name}'

    def get_absolute_url(self):
        return reverse('reminders:view_appointment', args=[str(self.id)])