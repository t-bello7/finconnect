from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate
from authentication.models import User, UserProfile

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60,label="Email", help_text='Required.Add a valid email address')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "password1", "password2"]

    @transaction.atomic 
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        user = UserProfile.objects.create(user=user)
        # user.interests.add(*self.cleaned_data.get('interests'))
        return user
        
class InstitutionSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_institution = True
        if commit:
            user.save()
        return user

class UserAuthenticateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Login")