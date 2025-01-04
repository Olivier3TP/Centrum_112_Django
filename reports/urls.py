from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    # Widok wyświetlający wszystkie zgłoszenia
    path('all/', views.all_reports_view, name='all_reports'),

    # Widok szczegółów zgłoszenia
    path('<int:report_id>/', views.report_detail_view, name='report_detail'),
]
