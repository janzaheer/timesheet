from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=200)
    admin = models.ForeignKey(
        'admins.Admin', blank=True, null=True,
        related_name='admin_projects',
        on_delete=models.SET_NULL
    )
    description = models.TextField(max_length=1000, blank=True, null=True)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Timesheet(models.Model):
    project = models.ForeignKey(
        Project, related_name='project_timesheets',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    expert = models.ForeignKey(
        'experts.Expert', related_name='expert_timesheet',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    title = models.CharField(max_length=200)
    details = models.TextField(
        max_length=1000, blank=True, null=True
    )
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
