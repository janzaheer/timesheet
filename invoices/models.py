from django.db import models
from django.utils import timezone
from projects .models import Project
from experts .models import Expert

class Invoice(models.Model):
    project = models.ForeignKey(
        Project, related_name='project_invoice',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    expert = models.ForeignKey(
        Expert , related_name='expert_invoice',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    invoice_company_name = models.CharField(max_length=200, null=True, blank=True)
    att_name = models.CharField(max_length=200, null=True, blank=True)
    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    name_of_consultant = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    tva_id = models.CharField(max_length=200, null=True, blank=True)
    name_of_bank = models.CharField(max_length=200, null=True, blank=True)
    address_of_bank = models.CharField(max_length=200, null=True, blank=True)
    account_no = models.CharField(max_length=200, null=True, blank=True)
    iban = models.CharField(max_length=200, null=True, blank=True)
    swift_code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.invoice_company_name
