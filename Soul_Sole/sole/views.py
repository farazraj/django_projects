from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render (request, 'signup.html')

def products(request):
    return render (request, 'products.html')

def thankyou(request):
    return render (request, 'thank_you.html')
