from django.contrib import admin
from APP.License.models import Vaccines, Growth_and_development
# Register your models here.


@admin.register(Vaccines)
class VaccinesAdmin(admin.ModelAdmin):
    list_display = ('Biological', 'Dose', 'Vaccine_date', 'Lot', 'Vaccinator_name',)


@admin.register(Growth_and_development)
class Growth_and_developmentAdmin(admin.ModelAdmin):
    list_display = ('Data','Doctor_name',)