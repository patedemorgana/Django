import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']   

        if password == password2:
            pass
        else:
            messages.info(request, 'Senhas não coincidem, tente de novo')
            return redirect(signup)
    else:
        return render(request, 'signup.html')
