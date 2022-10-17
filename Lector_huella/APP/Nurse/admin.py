from django.contrib import admin

# Register your models here.

from APP.Nurse.models import Nurses


@admin.register(Nurses)
class NursesAdmin(admin.ModelAdmin):
    list_display = ('data', 'Professional_card', 'Specialization',)