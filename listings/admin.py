from django.contrib import admin
from .models import Listings, Plans, InstitutionCategory , PlanCategory
# Register your models here.
admin.site.register(Listings)
admin.site.register(Plans)
admin.site.register(InstitutionCategory)
admin.site.register(PlanCategory)

