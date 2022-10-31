from django.contrib import admin
from django.urls import path,include
from sole import views

urlpatterns = [
    path("",views.home, name='home'),
    path("signin/", views.signin, name='signIn'),
    path("home/",views.home, name='home'),
    path("signup/",views.signup, name='signup'),
    path("products/",views.products, name='products')
]
