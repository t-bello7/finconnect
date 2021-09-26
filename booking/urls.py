from django.urls import path
from .views import BookingView

urlpatterns = [
    path('', BookingView.as_view(), name='booking')
]