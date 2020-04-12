import itertools 
from calendar import monthrange
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView, ListView, View
)
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.db import transaction
from django.db.models import Sum

from .models import Timesheet, TimeSheetRecord
from .forms import TimesheetForm, TimesheetRecordForm
from projects.models import Project
from django.http import Http404


MONTHS_CONTEXT = [
    (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'),
    (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'),
    (10, 'October'), (11, 'November'), (12, 'December')
]

YEARS_CONTEXT = [
    '2019', '2020', '2022', '2023', '2024', '2025', '2026', '2027',
    '2028', '2029', '2030',
]


class ExpertUserValidateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.request.user.user_expert:
                return super().dispatch(request, *args, **kwargs)    
        except:
            raise Http404('Page not found')


class TimesheetListView(LoginRequiredMixin, ExpertUserValidateMixin, ListView):
    template_name =  'projects/timesheet_list.html'
    model = Timesheet
    paginate_by = 100


class ProjectTimesheets(LoginRequiredMixin, ExpertUserValidateMixin, ListView):
    template_name = 'projects/project_timesheets.html'
    model = Timesheet
    paginate_by = 100

    def get_queryset(self):
        return Timesheet.objects.filter(
            project__id=self.kwargs.get('project_id'))



class TimesheetFormView(LoginRequiredMixin, ExpertUserValidateMixin, FormView):
    template_name = 'projects/timesheet_create.html'
    form_class = TimesheetForm

    def form_valid(self, form):
        with transaction.atomic():
            timesheet = form.save()

            month = int(self.request.POST.get('selected_month', '1'))
            year = int(self.request.POST.get('selected_year', '2020'))

            timesheet.month = month
            timesheet.year = year
            timesheet.save()
            
            total_days = monthrange(year, month)[1]

            for day in range(1, total_days+1):
                dt = timezone.datetime(year, month, day)
                weekday = dt.strftime('%A')

                TimeSheetRecord.objects.create(
                    timesheet=timesheet,
                    day=weekday,
                    date= '%d-%d-%d' % (year, month, day),
                    perdiem=timesheet.project.expert.perdiem 
                )

        return HttpResponseRedirect(reverse(
            'projects:project_timesheets',
            kwargs={'project_id': timesheet.project.id}
        ))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            project = Project.objects.get(id=self.kwargs.get('project_id'))
        except:
            raise Http404('Project Doesnot exists!')

        context["project"] = project
        context['months'] = MONTHS_CONTEXT
        context['years'] = YEARS_CONTEXT
        return context
    

class TimesheetUpdateView(LoginRequiredMixin, ExpertUserValidateMixin, UpdateView):
    template_name = 'projects/timesheet_update.html'
    form_class = TimesheetForm
    model = Timesheet

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('projects:timesheet_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all().order_by('name') 
        return context

class TimesheetRecordListView(LoginRequiredMixin, ExpertUserValidateMixin, ListView):
    template_name =  'projects/timesheet_record_list.html'
    model = TimeSheetRecord
    paginate_by = 100

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = TimeSheetRecord.objects.filter(
                timesheet__id=self.kwargs.get('pk'))

        return queryset.order_by('date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["timesheet"] = Timesheet.objects.get(id=self.kwargs.get('pk'))
        return context


class TimesheetRecordAllEditView(LoginRequiredMixin, ExpertUserValidateMixin, TemplateView):
    template_name = 'projects/all_records_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timesheet = Timesheet.objects.get(id=self.kwargs.get('timesheet_id'))
        timesheet_records = TimeSheetRecord.objects.filter(
            timesheet__id=self.kwargs.get('timesheet_id'))

        context["records"] = timesheet_records 
        context["timesheet"] = timesheet
        return context


class TimesheetRecordAllSaveView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist ('ids')
        dates = self.request.POST.getlist('date')
        day_workeds = self.request.POST.getlist('day_worked')
        place_of_activities = self.request.POST.getlist('place_of_activity')
        activities = self.request.POST.getlist('activities')

        for i, date, day_work, place_of_activity, activity in itertools.zip_longest(
            ids, dates, day_workeds, place_of_activities, activities):
            if i:
                record = TimeSheetRecord.objects.get(id=i)
                record.date=date
                record.day_worked=day_work
                record.place_of_activity=place_of_activity
                record.activities=activity
                record.save()
        return HttpResponseRedirect(reverse(
            'projects:project_timesheets',
            kwargs={'project_id': self.request.POST.get('project_id')}
        ))

class TimesheetReccordFormView(LoginRequiredMixin, ExpertUserValidateMixin, FormView):
    template_name = 'projects/timesheet_record_create.html'
    form_class = TimesheetRecordForm

    def form_valid(self, form):
        record=form.save()
        return HttpResponseRedirect(reverse('projects:timesheet_record_list',kwargs={'pk': record.timesheet.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["timesheet"] = Timesheet.objects.get(id=self.kwargs.get('pk'))
        return context

class TimesheetRecordUpdateView(LoginRequiredMixin, ExpertUserValidateMixin, UpdateView):
    template_name = 'projects/timesheet_record_update.html'
    form_class = TimesheetRecordForm
    model = TimeSheetRecord

    def form_valid(self, form):
        record=form.save()
        return HttpResponseRedirect(reverse('projects:timesheet_record_list',kwargs={'pk': record.timesheet.id}))


class TimeSheetInvoiceView(LoginRequiredMixin, ExpertUserValidateMixin, TemplateView):
    template_name = 'projects/time_sheet_view_invoice.html'

    def get_context_data(self, **kwargs):
        context = super(
            TimeSheetInvoiceView, self).get_context_data(**kwargs)

        try:
            invoice = Timesheet.objects.get(id=self.kwargs.get('pk'))
        except Timesheet.DoesNotExist:
            return Http404('Invoice does not exists in database')
        record = invoice.timesheet_record.all()

        try:
            total_worked_days = record.aggregate(
                total_days=Sum('day_worked'))
            total_worked_days = total_worked_days.get('total_days') or 0
        except:
            total_worked_days = 0

        try:
            total_expert_perdiem = record.filter(
                day_worked=1).aggregate(total_perdiem=Sum('perdiem'))
            print(total_expert_perdiem)
            total_expert_perdiem = total_expert_perdiem.get('total_perdiem') or 0
        except:
            total_expert_perdiem = 0

        context.update({
           'timesheet':invoice,
           'records': record

        })
        context["total_worked_days"] = total_worked_days
        context["total_expert_perdiem"] = total_expert_perdiem
        return context
