from django.contrib import admin
from APP.Patient.models import Patients
# Register your models here.


@admin.register(Patients)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'type_identification', 'identification_number', 'Phone', 'gender', 'Direction',)
    list_editable = ('Phone', 'gender',)
    search_fields = ('Name', 'identification_number',)