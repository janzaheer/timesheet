from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    ROLE_ADMIN = 'admin'
    ROLES = (
        ( ROLE_ADMIN, 'Admin' ),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    role = models.CharField(max_length=50, default=ROLE_ADMIN, choices=ROLES)

