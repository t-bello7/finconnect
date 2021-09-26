from django.contrib.auth import login,authenticate, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View
from .forms import UserSignUpForm,InstitutionSignUpForm, UserAuthenticateForm
from .decorators import user_required
import json
import re
from django.http import JsonResponse
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


User = get_user_model()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,}\b'

#handle username validation
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not (re.fullmatch(regex, email)):
            return JsonResponse({'email_error':'Email is not valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry email is in use, choose another one.'}, status=409)
        return JsonResponse({'email_valid':True})


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                # if user.is_active:
                login(request, user)
                return redirect('dashboard:homepage')
            print('invalid credentials')
            return render(request, 'authentication/login.html') 
            print('fill all fields')
        return render(request, 'authentication/login.html')
        
            

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/signup.html')
    
    def post(self, request):
        # get user data
        # validate
        # create a user account
        # keep the values in the fiels whrn validation is wrong
        full_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if not User.objects.filter(email=email).exists():
            if len(password) < 6:
                return render(request, 'authentication/signup.html', context )

            user = User.objects.create_user(full_name= full_name,email=email, password=password)
            user.set_password(password)
            # user.is_active = False
            user.save()
            current_site = get_current_site(request).domain
            # relativelink
            email_body = f'Hi {user.full_name}, Use link below to verify your email \n' 
            data = {
                'email_body': email_body, 
                'to_email': user.email,
                'email_subject': 'Verify your email', 
                'email_sender':'noreply@sem',
            }
            return redirect('authentication:login')

            # Util.send_email(data)
        return render(request, 'authentication/signup.html')


class LogoutView(View):

    def get(self, request):
        logout(request)
        ##send a logout message
        return redirect('authentication:login')



@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        context = {
            'user': user
        }
        return render(request, 'authentication/profile.html', context)