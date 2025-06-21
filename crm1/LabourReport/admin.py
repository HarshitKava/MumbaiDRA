from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Staff)
admin.site.register(CategoryOfDeployment)
admin.site.register(Structure)
admin.site.register(SiteEngDay)
admin.site.register(SiteEngNight)
admin.site.register(SLIDay)
admin.site.register(SLINight)
admin.site.register(CLIDay)
admin.site.register(CLINight)
admin.site.register(Area)
admin.site.register(ContractorDetail)
admin.site.register(AddLabour)
admin.site.register(LabourOfContractor)