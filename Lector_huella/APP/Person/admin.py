from django.contrib import admin

# Register your models here.
from APP.Person.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Cc', 'Phone','gender', 'Direction',)
    list_editable = ('Phone','gender',)
    search_fields = ('Name', 'Cc',)
