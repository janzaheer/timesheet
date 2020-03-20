from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView, ListView
)
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Timesheet
from .forms import TimesheetForm
from projects.models import Project


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
