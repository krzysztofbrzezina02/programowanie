from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ZapisyForm
# Create your views here.



def index(request):
    return render(request,'Home.html')

def Lekarz(request):
    lekar = Lekarze.objects.all()
    dane = {'lekar': lekar}
    return render(request,'Lekarz.html',dane)

def Przychodnia(request):
    o_nas = Lekarze.objects.all()
    dane = {'o_nas': o_nas}
    return render(request,'Przychodnia.html',dane)

def Kontakt(request):
    return render(request,'Kontakt.html')

def Zapisy_user(request):
    form = ZapisyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ZapisyForm()


    context = {
        'form': form
    }
    return render(request, "main/zapisy_create.html", context)
