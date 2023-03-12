from django.shortcuts import redirect, render
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import login, authenticate

from django.urls import reverse_lazy
from django.views.generic.edit import FormView 

def login1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')

            user =authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return render(request, 'blog_pages/inicio.html', {'mensaje': f'Bienvenido/a {user} al Blog'})
            else:
                return render(request, 'login/passornameincorrect.html', {'mensaje': 'Error, datos incorrectos'})
        else:
              return render(request, 'login/passornameincorrect.html', {'mensaje': 'Error, formulario erroneo'})  
    else:
        form = LoginForm()
    return render(request,'login/login.html', {'form': form})


def passornameincorrect(request):
    return render(request,'login/passornameincorrect.html' )

def register(request):
    if request.method == 'POST':

        form=UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'blog_pages/inicio.html',{"mensaje":"Usuario creado"})
    else:
        form=UserRegisterForm()

    return render(request, 'login/registro.html', {'form':form})

