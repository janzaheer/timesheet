from django.urls import path

from .views import (TimesheetListView, TimesheetFormView, TimesheetUpdateView,
    TimesheetRecordListView, TimesheetReccordFormView, TimesheetRecordUpdateView,
    TimeSheetInvoiceView, TimesheetRecordAllEditView, TimesheetRecordAllSaveView,
    ProjectTimesheets, AdminProjectReports, ExportInvoiceCsvView
)

urlpatterns = [
    path('timesheet/list', TimesheetListView.as_view(), name='timesheet_list'),
    path('<int:project_id>/timesheet', ProjectTimesheets.as_view(), name='project_timesheets'),
    path('<int:project_id>/timesheet/create', TimesheetFormView.as_view(), name='timesheet_create'),
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
    ),
    path(
        'timesheet/<int:pk>/invoice/view',
        TimeSheetInvoiceView.as_view(),
        name='timesheet_invoice_view'
    ),
     path(
        'timesheet/<int:timesheet_id>/edit/all/records',
        TimesheetRecordAllEditView.as_view(),
        name='timesheet_record_edit_all'
    ),
     path(
        'timesheet/save/all/records',
        TimesheetRecordAllSaveView.as_view(),
        name='timesheet_record_save_all'
    ),
    path(
        '<int:project_id>/reports',
        AdminProjectReports.as_view(),
        name='project_reports'
    ),
    path(
        '<int:project_id>/reports/export',
        ExportInvoiceCsvView.as_view(),
        name='project_reports_export'
    ),
]