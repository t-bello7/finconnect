from django.urls import path
from .Views import FaqView

urlpatterns = [
    path('', FaqView.as_view(), name='faq')
]
