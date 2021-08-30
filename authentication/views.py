from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserSignUpForm,InstitutionSignUpForm, UserAuthenticateForm
from .models import User
from .decorators import user_required



# Create your views here.
class SignUpView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    fields = '__all__'


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signupform.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')



class InstitutionSignUpView(CreateView):
    model = User
    form_class = InstitutionSignUpForm
    template_name = 'registration/signupform.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'institution'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


class LoginUser(LoginView):
    form_class = UserAuthenticateForm
    template_name = 'registration/login.html'
    # redirect_field_name = 'homepage'
    def get_success_url(self):
        """Here is the part where you can implement your login logic """

        return super().get_success_url()