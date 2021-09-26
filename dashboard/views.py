import json
import random
from django.views.generic import View
from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from authentication.decorators import user_required, institution_required
from django.shortcuts import render
from listings.models import Listings, Plans, InstitutionCategory
from django.http import JsonResponse
from listings.filter import InstituitionFilter
# Create your views here.
# @method_decorator([login_required, user_required], name='dispatch')
class SearchListingView(View):
    def get(self, request):
        # listings = Listings.object.filter(
        #     address__icontains=location
        # )
        return render(request, 'dashboard/list-search.html')
    def post(self, request):
        # search_string = json.loads(request.body).get('searchText')
        # institution = request.POST("category")
        # search_text = request.POST("searchText")
        # category = request.POST("category")
        # state = request.POST("state")
        search = request.POST["search_text"]
        
        listings = Listings.objects.filter(
            name__icontains=search)
        # ) | Listings.objects.filter(
        #     description__icontains=search_text
        # ) | Listings.objects.filter(
        #     address__icontains=address
        # ) | Listings.objects.filter(
        #     institution__icontains = institution
        # )
        context = {
            'listings': listings,
        }

        # data = listings.values()
        # return JsonResponse(list(data), safe=False )
        return render(request, 'dashboard/list-search.html', context)



class HomepageView(View):
    def get(self, request):
        listing_instance = Listings.objects.first()
        # listing_count = Listings.objects.all().filter(institution='CS').count()
        # for choice in listing_instance.INSTITUTION_CHOICES:
        categories = InstitutionCategory.objects.all()
        listings = list(Listings.objects.all())
        plans = Plans.objects.filter()
        mfilter = InstituitionFilter
        random_items = random.sample(listings, 8)

        context = {
            'plans': plans,
            'listings': random_items,
            'listing_instance': listing_instance,
            'instituition_categories': categories,
            'filter': mfilter,

        }
        return render(request, 'dashboard/homepage.html', context)

class DashboardView(View):
    def get(self, request):
        listings_created_by_user = Listings.objects.filter(list_id=request.user)
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


class AboutView(View):
    def get(self, request):

        return render(request, 'dashboard/about.html')


class ContactView(View):
    def get(self, request):

        return render(request, 'dashboard/contact.html')