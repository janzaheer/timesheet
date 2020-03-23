from django.db import models
from django.contrib.auth.models import User

class Expert(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    vat = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class ExpertUser(models.Model):
    user = models.OneToOneField(
        User, related_name='user_expert', on_delete=models.SET_NULL,
        blank=True, null=True
    )
    expert = models.OneToOneField(
        Expert, related_name='expert_user', on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.expert.name if self.expert else ''
    
