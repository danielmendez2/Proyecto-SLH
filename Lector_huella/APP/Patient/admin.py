from django.contrib import admin
from APP.Patient.models import Paciente
# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc', 'age', 'Phone', 'gender', 'Direction',)
    list_editable = ('Phone', 'gender',)
    search_fields = ('Name', 'Cc',)
