from django.contrib import admin
from APP.clinic_history.models import History
# Register your models here.


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc', 'Phone','gender', 'Direction',)
    list_editable = ('Phone','gender',)
    search_fields = ('Name', 'Cc',)