from django.urls import path

from .views import (
    AdminIndexView, AdminProjectFormView,
    AdminProjectUpdateView, AdminProjectDeleteView
)

urlpatterns = [
    path('index', AdminIndexView.as_view(), name='index'),
    path(
        'project/create', AdminProjectFormView.as_view(),
        name='admin_project_create'
    ),
    path(
        'project/<int:pk>/update', AdminProjectUpdateView.as_view(),
        name='admin_project_update'
    ),
    path(
        'project/<int:pk>/delete', AdminProjectDeleteView.as_view(),
        name='admin_project_delete'
    ),
]