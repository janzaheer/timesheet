from django.contrib.auth import forms as auth_forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(FormView):
    form_class = auth_forms.AuthenticationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
    
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:index'))

        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)

        return HttpResponseRedirect(reverse('common:index'))
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutView(RedirectView):
    def dispatch(self, request, *args, **kwargs):
        auth_logout(self.request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('common:login'))

