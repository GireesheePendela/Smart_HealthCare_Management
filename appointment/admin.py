from django.contrib import admin
from appointment.models import AppointmentDetails,BookedAppointment
admin.site.register(AppointmentDetails)
admin.site.register(BookedAppointment)