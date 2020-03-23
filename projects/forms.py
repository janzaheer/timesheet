from django import forms
from .models import Project, Timesheet, TimeSheetRecord


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = '__all__'


class TimesheetRecordForm(forms.ModelForm):
    class Meta:
        model = TimeSheetRecord
        fields = '__all__'
