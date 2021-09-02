from django.urls import path
from .views import LoginView, EmailValidationView, RegistrationView , LogoutView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),

    path('signup/', RegistrationView.as_view(), name="signup"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view())),
    # path('signup/student', UserSignUpView.as_view(), name='user_signup'),
    # path('signup/institution', InstitutionSignUpView.as_view(), name='institution_signup'),
]