from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, FormView, UpdateView, DeleteView, ListView
)
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin
from admins.views import AdminUserValidateMixin

from .models import Invoice
from .forms import InvoiceForm
from projects .models import Project
from experts .models import Expert


class InvoiceListView(LoginRequiredMixin, AdminUserValidateMixin, ListView):
    model = Invoice
    template_name = 'invoice/list_invoice.html'
    paginate_by = 100

class CreateInvoiceView(LoginRequiredMixin, AdminUserValidateMixin, FormView):
    form_class = InvoiceForm
    template_name = 'invoice/create_invoice.html'

    def form_valid(self, form):
        obj = form.save()
        obj.save()
        return HttpResponseRedirect(reverse('invoice:list'))

    def form_invalid(self, form):
        return super(CreateInvoiceView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateInvoiceView, self).get_context_data(**kwargs)
        project = (
            Project.objects.all()
        )
        expert = (
            Expert.objects.all()
        )
        context.update({
            'projects': project,
            'experts' : expert
        })
        return context


class InvoiceUpdateView(LoginRequiredMixin, AdminUserValidateMixin, UpdateView):
    template_name = 'invoice/update_invoice.html'
    form_class = InvoiceForm
    model =  Invoice

    def form_valid(self, form):
        expert = form.save()
        return HttpResponseRedirect(reverse('invoice:list'))
    
    def get_context_data(self, **kwargs):
        context = super(InvoiceUpdateView, self).get_context_data(**kwargs)
        project = (
            Project.objects.all()
        )
        expert = (
            Expert.objects.all()
        )
        context.update({
            'projects': project,
            'experts' : expert
        })
        return context

class InvoiceDetail(LoginRequiredMixin, AdminUserValidateMixin, TemplateView):
    template_name = 'invoice/view_invoice.html'

    def get_context_data(self, **kwargs):
        context = super(
            InvoiceDetail, self).get_context_data(**kwargs)

        try:
            invoice = Invoice.objects.get(id=self.kwargs.get('pk'))
        except Invoice.DoesNotExist:
            return Http404('Invoice does not exists in database')

        context.update({
           'invoice':invoice,
        })
        return context