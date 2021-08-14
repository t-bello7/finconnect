from django.contrib.auth import login,authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import UserSignUpForm
from .models import User
from .decorators import user_required



# Create your views here.


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user.hompage')



class InstitutionSignUpView(CreateView):
    model = User
    form_class = InstitutionSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data():
        kwargs['user_type'] = 'institution'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('instituition.dashboard')