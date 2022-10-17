from django.contrib import admin

from APP.Medico.models import medico


@admin.register(medico)
class medicoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
