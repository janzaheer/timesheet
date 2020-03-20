from django.contrib import admin

from .models import Admin, AdminUser

admin.site.register(Admin)
admin.site.register(AdminUser)
