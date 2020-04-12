from django.db import models
from django.utils import timezone
from experts.models import Expert


class Project(models.Model):
    name = models.CharField(max_length=200)
    admin = models.ForeignKey(
        'admins.Admin', blank=True, null=True,
        related_name='admin_projects',
        on_delete=models.SET_NULL
    )
    expert = models.ForeignKey(
        Expert,  blank=True, null=True,
        related_name='expert_project',
        on_delete=models.SET_NULL
    )
    service_number_contract = models.CharField(max_length=200, null=True, blank=True)
    internal_reference = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    name_of_company = models.CharField(max_length=200, null=True, blank=True)
    attention_mails = models.CharField(max_length=200, null=True, blank=True)
    address_company = models.CharField(max_length=200, null=True, blank=True)
    telephone_company = models.CharField(max_length=200, null=True, blank=True)
    vat_company = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    date_added = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.name


class Timesheet(models.Model):
    project = models.ForeignKey(
        Project, related_name='project_timesheets',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    title = models.CharField(max_length=200)
    details = models.TextField(
        max_length=1000, blank=True, null=True
    )
    month = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

class TimeSheetRecord(models.Model):
    DAY_MONDAY = 'monday'
    DAY_TUESDAY = 'tuesday'
    DAY_WEDNESDAY = 'wednesday'
    DAY_THRUSDAY = 'thrusday'
    DAY_FRIDAY = 'friday'
    DAY_SATURDAY = 'saturday'
    DAY_SUNDAY = 'sunday'

    DAY = (
        (DAY_MONDAY, 'monday'),
        (DAY_TUESDAY, 'tuesday'),
        (DAY_WEDNESDAY, 'wednesday'),
        (DAY_THRUSDAY, 'thrusday'),
        (DAY_FRIDAY, 'friday'),
        (DAY_SATURDAY, 'saturday'),
        (DAY_SUNDAY, 'sunday'),
    )
    timesheet = models.ForeignKey(
        Timesheet, related_name='timesheet_record',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    date = models.DateField(default=timezone.now, blank=True, null=True)
    day = models.CharField(
        max_length=200, choices=DAY, default=DAY_MONDAY,
        blank=True, null=True)
    day_worked = models.DecimalField(max_digits=4, decimal_places=2,
                                    default=0,blank=True, null=True
                                    )
    perdiem = models.DecimalField(max_digits=6, decimal_places=2,
                                    default=0,blank=True, null=True
                                    )
    place_of_activity = models.CharField(max_length=200, null=True, blank=True)
    activities = models.CharField(max_length=200, null=True, blank=True)
    total_month = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.timesheet.title 

    
