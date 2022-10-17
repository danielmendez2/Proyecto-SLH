from django.contrib import admin

from APP.Doctor.models import Doctors


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name',)
