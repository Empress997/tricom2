from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class ComplaintInformationAdmin(ImportExportActionModelAdmin):
    pass
    fieldsets = (
        ("Complaint Details", {"fields": ("cname", "address", "phone_number")}),
        ("Operator Details", {"fields": ("dname", "zone", "d_address","plate_number")}),
        ("Incident Details", {"fields": ("accident_date", "accident_time", "accident_place","violation_type","complaint_description","complaint_evidence","verification")}),
    )
    list_filter = ('created_at',)
    

admin.site.register(ComplaintInformation, ComplaintInformationAdmin)
admin.site.register(Profile)
admin.site.register(ContactUs)