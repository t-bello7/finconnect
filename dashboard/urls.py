from django.urls import path
from .views import DashboardView, HomepageView

urlpatterns = [
    # path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('', HomepageView.as_view(), name='homepage')
]