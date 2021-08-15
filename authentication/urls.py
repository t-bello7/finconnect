from django.urls import path
from .views import UserSignUpView, InstitutionSignUpView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signup/student', UserSignUpView.as_view(), name='user_signup'),
    path('signup/institution', InstitutionSignUpView.as_view(), name='instution_signup'),
]