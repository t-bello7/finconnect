from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from authentication.models import User, UserProfile

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required.Add a valid email address')
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ("email", "username", "password1", "password2")

    @transactionn.atomic 
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        user = Student.objects.create(user=user)
        user.interests.add(*self.cleaned_data.get('interests'))
        return user
        
class InstitutionSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_institution = True
        if commit:
            user.save()
        return user