from django.urls import path

from .views import InvoiceListView,CreateInvoiceView, InvoiceUpdateView, InvoiceDetail

urlpatterns = [
    path('create/', CreateInvoiceView.as_view(), name='invoice_create'),
    path('list', InvoiceListView.as_view(), name='list'),
    path(
        '<int:pk>/update/', InvoiceUpdateView.as_view(),
        name='update'
    ),
     path(
        '<int:pk>/view', InvoiceDetail.as_view(),
        name='detial'
    ),
]
