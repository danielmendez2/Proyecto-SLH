from django.contrib import admin
from APP.user.models import User
# Register your models here.
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
   list_display = ('email',)
   readonly_fields = ["date_joined"]
   fieldsets = (
      (None, {'fields': ('email', 'password', 'groups',)}),
      ('Permissions', {'fields': ('is_staff', 'is_active')}),
   )
   add_fieldsets = (
      (None, {
         'classes': ('wide',),
         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
       ),
   )
   search_fields = ('email',)
   ordering = ('email',)

