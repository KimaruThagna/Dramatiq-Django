from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Appointment
# Create your views here.

class AppointmentListView(ListView):
    model = Appointment


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentUpdateView(SuccessMessageMixin, UpdateView):

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully updated.'


class AppointmentDeleteView(DeleteView):
    """Prompts users to confirm deletion of an appointment"""

    model = Appointment
    success_url = reverse_lazy('list_appointments')
    
class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new appointment"""

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully created.'
