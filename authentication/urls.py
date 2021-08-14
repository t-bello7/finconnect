from django.urls import path

urlspatterns = [
    path('signup/', classroom.SignUpView.as_view(), name="signup"),

]