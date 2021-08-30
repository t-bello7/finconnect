from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
from helpers.models import TrackingModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    PermissionsMixin, UserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime, timedelta
# from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class MyUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        """
        Create and save a user with the given username, email and password.

        """
        if not email:
            raise valueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email=None, Password=None, **extra_field):
        extra_field.setdefault('is_staff', False)
        extra_field.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser mus have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    An abstract base class implementing a fully featured User Model with admin-compliant permissions.
    Automatically created username that can be changed 
    # """
    # username_validator = UnicodeUsernameValidator()
    username = models.CharField(_('username'), max_length=150)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email_address'), blank=True, unique=True)
    last_login = models.CharField(max_length=100,default=timezone.now())
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    is_institution = models.BooleanField(
        _('user is institution'),
        default=False,
        help_text=_(
            'Checkes if the user is an institution'
        )
    )
    is_user = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether the user can log into this admin site'
        )
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_verified = models.BooleanField(
        _('email_verified'),
        default=False,
        help_text=_(
            'Designates whether this users email is verified.'
        )
    )
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    
    # @property
    # def token(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
    #     }

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    def set_username(sender, instance, **kwargs):
        if not instance.username:
            username = instance.first_name
            counter=1
            while User.objects.filter(username=username):
                username = instance.first_name + str(counter)
                counter += 1
            instance.username = username
    models.signals.pre_save.connect(set_username, sender=settings.AUTH_USER_MODEL)

class institutinProfile(models.Model):
    pass


