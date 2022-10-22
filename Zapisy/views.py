from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ZapisyForm
from .forms import FormularzForm
from django.contrib.auth import logout
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
# Create your views here.



def index(request):
    nowy=Aktualnosci.objects.all()
    dane = {'nowy': nowy}
    return render(request,'Home.html',dane)

def Lekarz(request):
    nowy=Aktualnosci.objects.all()
    lekar = Lekarze.objects.all()
    dane = {'lekar': lekar,'nowy': nowy}
    return render(request,'Lekarz.html',dane)

def Przychodnia(request):
    nowy=Aktualnosci.objects.all()
    o_nas = Lekarze.objects.all()
    dane = {'o_nas': o_nas,'nowy': nowy}
    return render(request,'Tytulowa.html',dane)

def Zapisy_user(request):
    nowy=Aktualnosci.objects.all()
    form = ZapisyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ZapisyForm()


    context = {
        'form': form,'nowy':nowy
    }
    return render(request, "main/zapisy_create.html", context)

#def Kontakt(request):

 #return render(request,'Kontakt.html')



def Formularz(request):
    nowy=Aktualnosci.objects.all()
    form = FormularzForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormularzForm()


    context = {
        'form': form,'nowy':nowy
    }
    return render(request, "main/formularz.html", context)


#def register(request):
    #form = UserRegistrationForm(request.POST or None)
    #if form.is_valid():
       # form.save()
        #form = UserRegistrationForm()




    #context = {
     #   'form': form
    #}

    #return render(request, 'registration/register.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect("http://127.0.0.1:8000/profil/")
            else:
               raise forms.ValidationError("Looks like a username with that email or password already exists")

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form' : form})

def profil(request):
    nowy=Aktualnosci.objects.all()
    dane = {'nowy': nowy}
    return render(request, "zalogowani/profil.html",dane)
