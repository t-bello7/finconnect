from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from authentication.decorators import user_required, institution_required

# Create your views here.
@method_decorator([login_required, user_required], name='dispatch')
class HomepageView(CreateView):
    pass


@method_decorator([login_required, institution_required], name='dispatch')
class DashboardView(CreateView):
    pass