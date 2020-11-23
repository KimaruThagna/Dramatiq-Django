"""Dramatiq_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'reminders'

urlpatterns = [
    path('new', AppointmentCreateView.as_view(), name='new_appointment'),
    path('', AppointmentListView.as_view(), name='list_appointments'),
    path(r'^(?P<pk>[0-9]+)/edit$', AppointmentUpdateView.as_view(), name='edit_appointment'),
    path(r'^(?P<pk>[0-9]+)$', AppointmentDetailView.as_view(), name='view_appointment'),

    path(r'^(?P<pk>[0-9]+)/delete$', AppointmentDeleteView.as_view(), name='delete_appointment'),
]
