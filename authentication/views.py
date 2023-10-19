from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def singup(request):
    return render(request, "authnetication/signup.html")

def singin(request):
    return render(request, "authnetication/signin.html")

def singout(request):
    pass