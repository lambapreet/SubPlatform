from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(UserCreationForm):
    class meta:
        model = CustomUser
        fields = ['email', 'first_name','last_name','password1','password2','is_writer']
