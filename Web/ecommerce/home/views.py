from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.write("<h1>Welcome to ecommerce web</h1>")
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')