from django.urls import path
from .views import FaqView
from .apps import FaqConfig

app_name = FaqConfig.name

urlpatterns = [
    path('', FaqView.as_view(), name='faq')
]
