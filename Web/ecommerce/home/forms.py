from django.forms import ModelForm
from .models import ProductExample, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ProductForm(ModelForm):
    class Meta:
        model = ProductExample
        fields = ['name', 'price']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email',]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email',]