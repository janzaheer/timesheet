from django import forms
from .models import Project, Timesheet, TimeSheetRecord


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean_experts(self):
        return self.data.getlist('experts')


class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = '__all__'


class TimesheetRecordForm(forms.ModelForm):
    class Meta:
        model = TimeSheetRecord
        fields = '__all__'
