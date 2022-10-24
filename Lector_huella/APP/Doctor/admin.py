from django.contrib import admin

from APP.Doctor.models import Doctors


@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc', 'Phone','Direction', 'gender', 'email', 'Professional_card')
    list_filter = ('Name', 'Cc')
    list_editable = ('Phone', 'Direction', 'email')
