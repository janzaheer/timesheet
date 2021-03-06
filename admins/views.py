from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView
)

from projects.models import Project
from projects.forms import ProjectForm
from projects.models import Expert


class AdminUserValidateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.request.user.user_admin:
                return super().dispatch(request, *args, **kwargs)    
        except:
            raise Http404('Page not found')
    


class AdminIndexView(LoginRequiredMixin, AdminUserValidateMixin, TemplateView):
    template_name = 'admins/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.filter(
            admin=self.request.user.user_admin.admin).order_by('-id')
        return context


class AdminProjectFormView(LoginRequiredMixin, AdminUserValidateMixin, FormView):
    template_name = 'admins/create_admin_project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('admins:index'))

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experts"] = Expert.objects.all()
        return context


class AdminProjectUpdateView(LoginRequiredMixin, AdminUserValidateMixin, UpdateView):
    template_name = 'admins/update_admin_project.html'
    form_class = ProjectForm
    model = Project

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('admins:index'))
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experts"] = Expert.objects.all()
        context["project_experts"] = self.object.experts.values_list('id', flat=True)
        return context


class AdminProjectDeleteView(LoginRequiredMixin, AdminUserValidateMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('admins:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
