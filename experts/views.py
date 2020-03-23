from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView, ListView
)
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin

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
            'name': self.request.POST.get('full_name'),
            'mobile': self.request.POST.get('mobile'),
            'position': self.request.POST.get('position'),
            'category': self.request.POST.get('category'),
            'address': self.request.POST.get('address'),
            'vat': self.request.POST.get('uat'),
        }
        expertform = ExpertForm(expert_kwargs)
        if expertform.is_valid:
            expert = expertform.save()
            ExpertUser.objects.create(user=user, expert=expert)
        
        return HttpResponseRedirect(reverse('experts:expert_list'))


class ExpertUpdateView(LoginRequiredMixin, AdminUserValidateMixin, UpdateView):
    template_name = 'experts/experts_update.html'
    form_class = ExpertForm
    model =  Expert

    def form_valid(self, form):
        expert = form.save()
        return HttpResponseRedirect(reverse('experts:expert_list'))
