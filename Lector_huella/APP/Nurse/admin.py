from django.contrib import admin

# Register your models here.

from APP.Nurse.models import Nurses


@admin.register(Nurses)
class NursesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc','Phone', 'Direction', 'gender', 'email','Professional_card')
    list_filter = ('Name', 'Cc')
    list_editable = ('Phone', 'Direction', 'email')