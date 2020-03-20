from django.urls import path

from .views import ExpertsListView, ExpertCreateFormView, ExpertUpdateView

urlpatterns = [
    path('list', ExpertsListView.as_view(), name='expert_list'),
    path('create', ExpertCreateFormView.as_view(), name='experts_create'),
    path(
        '<int:pk>/update/', ExpertUpdateView.as_view(),
        name='experts_update'
    ),
]
