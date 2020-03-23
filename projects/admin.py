from django.contrib import admin

from .models import Project, Timesheet, TimeSheetRecord

admin.site.register(Project)
admin.site.register(Timesheet)
admin.site.register(TimeSheetRecord)

