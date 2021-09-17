import django_filters

from .models import *


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listings
        fields = ['address', 'description']


class InstituitionFilter(django_filters.FilterSet):
    class Meta:
        model = InstitutionCategory
        fields = ['name']