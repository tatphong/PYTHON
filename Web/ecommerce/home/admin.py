from django.contrib import admin
from .models import ProductExample
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','image']
    list_filter = ['price']
    search_fields = ['name']
admin.site.register(ProductExample,ProductAdmin)