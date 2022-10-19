from django.contrib import admin
from APP.clinic_history.models import History
# Register your models here.


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Occupation', 'hour_entry_finish')
    search_fields = ('Name',)