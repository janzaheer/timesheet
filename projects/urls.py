from django.urls import path

from .views import TimesheetListView, TimesheetFormView, TimesheetUpdateView

urlpatterns = [
    path('timesheet/list', TimesheetListView.as_view(), name='timesheet_list'),
    path('timesheet/create', TimesheetFormView.as_view(), name='timesheet_create'),
    path(
        'timesheet/<int:pk>/update',
        TimesheetUpdateView.as_view(),
        name='timesheet_update'
    ),
]