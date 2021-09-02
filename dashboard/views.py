from django.views.generic import View
from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from authentication.decorators import user_required, institution_required
from django.shortcuts import render
from listings.models import Listings, Plans
# Create your views here.
# @method_decorator([login_required, user_required], name='dispatch')
class HomepageView(View):
    def get(self, request):
        context = {
            'plans': Plans.objects.filter(),
            'listings': Listings.objects.filter(),
        }
        return render(request, 'dashboard/homepage.html', context)