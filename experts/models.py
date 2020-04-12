from django.db import models
from django.contrib.auth.models import User

class Expert(models.Model):
    name = models.CharField(max_length=200)
    sur_name = models.CharField(max_length=20, blank=True, null=True)
    vat_expert = models.CharField(max_length=100, blank=True, null=True)
    email_expert = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    name_of_bank = models.CharField(max_length=200, null=True, blank=True)
    address_of_bank = models.CharField(max_length=200, null=True, blank=True)
    account_no = models.CharField(max_length=200, null=True, blank=True)
    iban = models.CharField(max_length=200, null=True, blank=True)
    swift_code = models.CharField(max_length=200, null=True, blank=True)
    daily_fee =  models.DecimalField(
        max_digits=100, decimal_places=2,
        default=0, blank=True, null=True
    )
    perdiem =  models.DecimalField(
        max_digits=100, decimal_places=2,
        default=0, blank=True, null=True
    )
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
    
