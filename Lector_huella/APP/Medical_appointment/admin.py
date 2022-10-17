from django.contrib import admin
from APP.Medical_appointment.models import Quotes
# Register your models here.


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('doctors', 'patient', 'date_and_time',)
    list_editable = ('date_and_time',)
    search_fields = ('patient',)