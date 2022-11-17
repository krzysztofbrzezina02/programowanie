from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ZapisyForm,RegistrationForm
from .forms import FormularzForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets
# Create your views here.



def index(request):
    return render(request,'Strona_Główna.html')

def Lekarz(request):
    lekar = Lekarze.objects.all()
    dane = {'lekar': lekar}
    return render(request,'Lekarz.html',dane)

def Przychodnia(request):
    o_nas = Lekarze.objects.all()
    dane = {'o_nas': o_nas}
    return render(request,'Przychodnia_pacjentów.html',dane)



def Zapisy_user(request):
    form = ZapisyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ZapisyForm()


    dane = {
        'form': form,
    }

    return render(request, "main/zapisy_create.html", dane)



def Formularz(request):
    form = FormularzForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormularzForm()


    dane = {
        'form': form,
    }
    return render(request, "Kontakt.html", dane)

def profil(request):
    return render(request, "zalogowani/profil.html")

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profil')
    else:
        form = RegistrationForm()

    return render(request,'registration/sign_up.html',{"form":form})





