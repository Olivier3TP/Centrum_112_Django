from django.urls import path
from account import views

urlpatterns = [
    #url logowania
    #url medyk_dashboard
    #url_dispatcher_dashboard

]



app_name = 'accounts'

urlpatterns = [
    # Widok zgłoszeń przypisanych do medyka
    path('medic/reports/', views.medic_reports_view, name='medic_reports'),
]