from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView, ListView
)
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project
from .models import Expert, ExpertUser
from .forms import ExpertForm
from admins.views import AdminUserValidateMixin


class ExpertsListView(LoginRequiredMixin, AdminUserValidateMixin, ListView):
    model = Expert
    template_name = 'experts/experts_list.html'
    paginate_by = 100


class ExpertCreateFormView(LoginRequiredMixin, AdminUserValidateMixin, FormView):
    template_name = 'experts/experts_create.html'
    form_class = auth_forms.UserCreationForm

    def form_valid(self, form):
        user = form.save()
        expert_kwargs = {
            'name': self.request.POST.get('name'),
            'sur_name': self.request.POST.get('sur_name'),
            'vat_expert': self.request.POST.get('vat_expert'),
            'email_expert': self.request.POST.get('email_expert'),
            'mobile': self.request.POST.get('mobile'),
            'daily_fee': self.request.POST.get('daily_fee'),
            'perdiem': self.request.POST.get('perdiem'),
            'address': self.request.POST.get('address'),
            'name_of_bank': self.request.POST.get('name_of_bank'),
            'address_of_bank': self.request.POST.get('address_of_bank'),
            'account_no': self.request.POST.get('account_no'),
            'iban': self.request.POST.get('iban'),
            'swift_code': self.request.POST.get('swift_code')        }
        expertform = ExpertForm(expert_kwargs)
        if expertform.is_valid:
            expert = expertform.save()
            ExpertUser.objects.create(user=user, expert=expert)
        
        return HttpResponseRedirect(reverse('experts:expert_list'))


class ExpertUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'experts/experts_update.html'
    form_class = ExpertForm
    model =  Expert

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('experts:expert_projects'))


class ExpertProjects(LoginRequiredMixin, ListView):
    model = Project
    paginate_by = 100
    template_name = 'projects/expert_projects.html'
    
    def get_queryset(self):
        return self.request.user.user_expert.expert.project_experts.all().order_by('name')
