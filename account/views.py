# Create your views here.

# widok logowania i przekierowanie na strony
# (jezeli loguje sie medyk to na medic_dashboard a jezeli dyspozytor to dispatcher_dashboard)
#
# widok dyspozytora:
# - dashboard(wszystkie zgloszenia)
# - pojednycze zgloszenie

from django.shortcuts import render, get_object_or_404
from reports.models import Report
from django.contrib.auth.decorators import login_required

def all_reports_view(request):
    reports = Report.objects.all().order_by('id')
    return render(request, 'reports/all_reports.html', {'reports': reports})


def report_detail_view(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})
#
# widok medykow
# - przypisane zgloszenia
@login_required
def medic_reports_view(request):
    if request.User.role != 'medic':
        return render(request, 'account/403.html', status=403)

    medic_username = request.user.username
    reports = Report.objects.filter(medic__username=medic_username).select_related('dispatcher')

    return render(request, 'account/medic_reports.html', {'reports': reports})
#
# do widokow dyspozytora i medyka nie da sie dostac bez zalogowania
# jak bys mial jakis problem to edytuj model ale chyba nie bedzie trzeba