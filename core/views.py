from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
# Create your views here.
from .models import Animal

@login_required(login_url='/login/')


def lista_todos_animais(request):
    animal = Animal.objects.filter(ativo=True)
    return render(request, 'lista.html', {'animal':animal})


def login_user(request):
    return render(request, 'login.html')

def logout_user(request):

    logout(request)
    return redirect('/login')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou Senha inválidos. Por favor tente novamente.')
    return redirect('/login/')
