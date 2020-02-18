from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Member

# Register your models here.
admin.site.register(Member)

class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'Member'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)