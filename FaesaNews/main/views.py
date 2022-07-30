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
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email já é cadastrado')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Usuário já é cadastrado')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #Loga o usuário e redireciona ele pra página de configuração
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #Cria um perfil pro usuário
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Senhas não coincidem, tente de novo')
            return redirect(signup)
    else:
        return render(request, 'signup.html')
