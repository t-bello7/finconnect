from django.urls import path
from .views import UserSignUpView, InstitutionSignUpView, SignUpView, LoginUser

urlpatterns = [
    path('login/',LoginUser.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signup/student', UserSignUpView.as_view(), name='user_signup'),
    path('signup/institution', InstitutionSignUpView.as_view(), name='institution_signup'),
]