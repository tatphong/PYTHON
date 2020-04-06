from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index/', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('auth/', views.loginuser, name="loginuser"),
    path('login/', views.loginuser, name="login"),
    path('logoutuser/', views.logoutuser, name="logoutuser"),
    path('product/', views.product, name="product"),
]