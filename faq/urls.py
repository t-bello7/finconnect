from django.urls import path
from .views import FaqView

urlpatterns = [
    path('', FaqView.as_view(), name='faq')
]
