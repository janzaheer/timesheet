from django.urls import path

from .views import (TimesheetListView, TimesheetFormView, TimesheetUpdateView,
 TimesheetRecordListView, TimesheetReccordFormView, TimesheetRecordUpdateView)

urlpatterns = [
    path('timesheet/list', TimesheetListView.as_view(), name='timesheet_list'),
    path('timesheet/create', TimesheetFormView.as_view(), name='timesheet_create'),
    path(
        'timesheet/<int:pk>/update',
        TimesheetUpdateView.as_view(),
        name='timesheet_update'
    ),
    path('timesheet/record/<int:pk>/list', TimesheetRecordListView.as_view(), name='timesheet_record_list'),
    path('timesheet/create/<int:pk>/record', TimesheetReccordFormView.as_view(), name='timesheet_record_create'),
     path(
        'timesheet/<int:pk>/update/record',
        TimesheetRecordUpdateView.as_view(),
        name='timesheet_record_update'
    )
]