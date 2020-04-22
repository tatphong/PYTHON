from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import ProductForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ProductExample

# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.write("<h1>Welcome to ecommerce web</h1>")
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'pages/auth.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'pages/auth.html', {'form':AuthenticationForm, 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required
def product(request):
    products = ProductExample.objects.all()
    return render(request, 'pages/product.html', {'products': products})

    
    