from django.shortcuts import render
from django.views.generic import View
from .models import Plans, Listings

# Create your views here.
class ListView(View):
    def get(self, request):
        return render(request, 'listings/list_form.html')