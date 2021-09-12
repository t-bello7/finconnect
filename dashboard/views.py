from django.views.generic import View
from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from authentication.decorators import user_required, institution_required
from django.shortcuts import render
from listings.models import Listings, Plans
import json
from django.http import JsonResponse
# Create your views here.
# @method_decorator([login_required, user_required], name='dispatch')
class SearchListingView(View):
    def get(self, request):
        # listings = Listings.object.filter(
        #     address__icontains=location
        # )
        return render(request, 'dashboard/list-search.html')
    def post(self, request):
    # list_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # name = models.CharField(max_length=100)
    # institution = models.CharField(max_length=2, choices=INSTITUTION_CHOICES)
    # address = models.CharField(max_length=150)
        search_string = json.loads(request.body).get('searchText')
        listings = Listings.objects.filter(
            institution__startswith=search_string
        ) | Listings.objects.filter(
            description__icontains=search_string
        ) | Listings.objects.filter(
            address__icontains=search_string
        ) | Listings.objects.filter(
            institution__icontains = search_string
        )

        data = listings.values()
        return JsonResponse(list(data), safe=False )



class HomepageView(View):
    def get(self, request):
        listing_instance = Listings.objects.first()
        # listing_count = Listings.objects.all().filter(institution='CS').count()
        # for choice in listing_instance.INSTITUTION_CHOICES:

        context = {
            'plans': Plans.objects.filter(),
            'listings': Listings.objects.filter(),
            'listing_instance': listing_instance
        }
        return render(request, 'dashboard/homepage.html', context)

class DashboardView(View):
    def get(self, request):
        listings_created_by_user = Listings.objects.filter(list_id=request.user)
        print(listings_created_by_user)
        context = {
            'listings': listings_created_by_user
        }
        return render(request, 'dashboard/dashboard.html', context)

class ListDetailView(View):  
    def get(self, request, pk):
        # id = request.GET.get('pk')
        context = {
            'listings' : Listings.objects.filter(pk=pk)
        }
        print(Listings.objects.filter(pk=pk))

        # context["data"] = GeeksModel.objects.get(id =id)
        return render(request, 'dashboard/list-detail.html', context)
