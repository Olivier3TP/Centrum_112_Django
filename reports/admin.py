from django.contrib import admin
from reports.models import Report


# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'description')
    search_fields = ('first_name', 'last_name', 'address', 'description')
    list_filter = ('first_name', 'last_name')

admin.site.register(Report, ReportAdmin)
