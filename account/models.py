from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    is_writer = models.BooleanField(default=False, verbose_name="Are you a writer?")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
