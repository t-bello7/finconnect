from django.shortcuts import render
from django.generic.views import View

# Create your views here.

class FaqView(View):
    def get(self, request):
        return render(request, 'faq/faq.html')