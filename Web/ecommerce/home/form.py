from django.forms import ModelForm
from .models import ProductExample

class ProductForm(ModelForm):
    class Meta:
        model = ProductExample
        fields = ['name', 'price']