from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic import View
from .models import Plans, Listings, InstitutionCategory, PlanCategory
import json
from django.http import JsonResponse
from .forms import ListingsForm

# Create your views here.

class SearchListing(View):
    
    def post(self, request):
    # list_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # name = models.CharField(max_length=100)
    # institution = models.CharField(max_length=2, choices=INSTITUTION_CHOICES)
    # address = models.CharField(max_length=150)
        search_string = json.loads(request.body).get('searchText')
        listing = Listings.objects.filter(
            institution__starts_with=search_string)
        context ={
            'listing': listing
        }
        return render(request, 'dashboard/search-listings', context)
class CheckBoxView(View):
    def post(self, request):
        data = json.loads(request.body)
        check_box = data['checkbox']
        if check_box % 2 == 1:
            return JsonResponse({'check_valid':'Check Box Available'}, status=200)
        return JsonResponse({'check_invalid':True})

class InstitutionView(View):
    def get(self, request):
        listing_instance = Listings.objects.first()
        institution_categories = InstitutionCategory.objects.all()
        context = {
            'listing_instance': listing_instance,
            'institution_categories':institution_categories
        }
        return render(request, 'listings/add-institution.html', context)

    def post(self, request):
        name = request.POST['name']
        description = request.POST['description']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        address = f'{street}{city}{state},{country}'
        start_time = request.POST['start_time']
        close_time = request.POST['close_time']
        # sat_work_hours = request.POST['sat_available']
        institution = request.POST['institution']
        image = request.FILES['image']
        #     sat_work_hours = json.loads({'sat':'off'})
        # # data = json.loads(request.body).get('satWok')
        # check_box = data['checkbox']
        # if sat_work_hours ==  'on':
        #     start_time_sat = request.POST['sat_start_time']
        #     close_time_sat = request.POST['sat_close_time']
        Listings.objects.create(list_id=request.user, name=name, description=description, address=address , start_time=start_time, close_time=close_time,institution=institution, list_image=image)
        # start_time = start_time, is_saturday_available = True ,close_time = close_time, start_time_sat = start_time_sat, close_time_sat= close_time_sat,institution=institution,)
        # else:
        #     Listings.objects.create(owner=request.user, name=name, description=description, address=address, 
        # start_time = start_time, is_saturday_available = False ,close_time = close_time, start_time_sat = start_time_sat, close_time_sat= close_time_sat,institution=institution,)

        # listing_instance = Listings.objects.first()
        # context = {
        #     'listing_instance': listing_instance
        # }
    
        return redirect('dashboard')
    
class UpdateListingView(View):
    def get(self, request, pk):
        context = {}

        #fetch the object 
        obj = get_object_or_404(Listings, id=pk)

        form = ListingsForm(request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponeRedirect("/"+id)
        
        context["form"] = form

        return render(request, "listings/update-listing.html", context)

        


class PlanView(View):
    def get(self, request):
        return render(request, 'listing/add-institution.html')

    def post(self, request):
        plan = request.POST['plan_type']
        plan_name = request.POST['plan_name']
        plan_description = request.POST['plan_description']
        price = request.POST['price']
        rate = request.POST['rate']
        image = request.POST['plan_image']
        return render(request, 'listings/add-institution.html')

class AddSuccessView(View):
    def get(self, request):
        return render(request, 'listings/add-success.html')