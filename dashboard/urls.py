from django.urls import path
from .views import HomepageView, DashboardView,SearchListingView, ListDetailView, ContactView, AboutView
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from .apps import DashboardConfig

app_name = DashboardConfig.name
urlpatterns = [
    # path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('', HomepageView.as_view(), name='homepage'),
    path('dashboard/', login_required(DashboardView.as_view()), name='list'),
    path('search-listings/',SearchListingView.as_view(), name='search-list'),
    path('<int:pk>/', ListDetailView.as_view(),name='list-detail'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    # path('<str:location>', ListDetailView.as_view(), name='list-location')
]