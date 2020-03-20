from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView
)

from projects.models import Project
from projects.forms import ProjectForm


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
        project = form.save()
        if self.request.POST.get('status_set') == 'True':
            project.status = True
        elif self.request.POST.get('status_set') == 'False':
            project.status = False
        project.save()

        return HttpResponseRedirect(reverse('admins:index'))

    def form_invalid(self, form):
        return super().form_invalid(form)


class AdminProjectUpdateView(LoginRequiredMixin, AdminUserValidateMixin, UpdateView):
    template_name = 'admins/update_admin_project.html'
    form_class = ProjectForm
    model = Project

    def form_valid(self, form):
        if self.request.POST.get('status_set') == 'True':
            project.status = True
        elif self.request.POST.get('status_set') == 'False':
            project.status = False
        project.save()

        return HttpResponseRedirect(reverse('admins:index'))
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class AdminProjectDeleteView(LoginRequiredMixin, AdminUserValidateMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('admins:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
