from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    user = models.OneToOneField(
        User, related_name="user_admin", on_delete=models.SET_NULL,
        blank=True, null=True
    )
    admin = models.OneToOneField(
        Admin, related_name="admin_user", on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.admin.name if self.admin else ''

