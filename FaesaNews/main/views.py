import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']   
    else:
        return render(request, 'signup.html')
