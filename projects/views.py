from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView, ListView
)
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Timesheet, TimeSheetRecord
from .forms import TimesheetForm, TimesheetRecordForm
from projects.models import Project
from django.http import Http404



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


class TimesheetFormView(LoginRequiredMixin, ExpertUserValidateMixin, FormView):
    template_name = 'projects/timesheet_create.html'
    form_class = TimesheetForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('projects:timesheet_list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all().order_by('name') 
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
        print(record)
        print("______________________________________")
        context.update({
           'invoice':invoice,
           'records': record

        })
        return context
