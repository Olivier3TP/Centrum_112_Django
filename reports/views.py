from django.shortcuts import render, redirect
from reports.forms import ReportForm
# Create your views here.
def report_view(request):
    thank_you = False
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            thank_you = True
            form = ReportForm()
    else:
        form = ReportForm()

    return render(request, 'reports/report_form.html', {'form': form, 'thank_you': thank_you})