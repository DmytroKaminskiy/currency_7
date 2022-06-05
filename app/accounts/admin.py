from django.contrib import admin

from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    filter_horizontal = ('groups', 'user_permissions')
    # user.groups.filter(name='Manager').count()


admin.site.register(User, UserAdmin)
