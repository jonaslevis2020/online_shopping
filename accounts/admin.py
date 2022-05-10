from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name', 'user_name')
    readonly_fields = ['date_joined', 'last_login']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['-date_joined']


admin.site.register(Account, AccountAdmin)
# admin.site.register(AccountAdmin)