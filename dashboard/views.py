from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from authentication.decorators import user_required, institution_required
from .models import Listing
# Create your views here.
# @method_decorator([login_required, user_required], name='dispatch')
class HomepageView(ListView):
    model = Listing
    template_name = 'dashboard/homepage.html'


# @method_decorator([login_required, institution_required], name='dispatch')
class DashboardView():
    pass