from django.urls import path
from .views import BokkingView

urlpatterns = [
    path('', BokkingView.as_view(), name='booking')
]