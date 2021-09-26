from django.urls import path
from .views import LoginView, EmailValidationView, RegistrationView , LogoutView, ProfileView
from django.views.decorators.csrf import csrf_exempt
# from .apps import AuthenticationConfig

# app_name = AuthenticationConfig.name

urlpatterns = [
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view())),
    path('profile/', ProfileView.as_view(), name='profile'),
]