from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .models import Zapisy
from .forms import ProductForm
# Create your views here.



def index(request):
    zapis = Zapisy.objects.all()
    specja = Specjalizacje.objects.all()
    dane = {'zapis': zapis, 'specja': specja}
    return render(request,'Home.html',dane)

#def Specjalizacja(request,id):
 #   zawiera = Specjalizacje.objects.get(pk=id)
  #  return HttpResponse(zawiera)

def Zapisu(request,id):
    zawiera = Zapisy.objects.get(pk=id)
    dane = {'zawiera': zawiera}
    return render(request,'Zapisu.html',dane)


def Lekarz(request):
    lekar = Lekarze.objects.all()
    dane = {'lekar': lekar}
    return render(request,'Lekarz.html',dane)

def Przychodnia(request):
    o_nas = Lekarze.objects.all()
    dane = {'o_nas': o_nas}
    return render(request,'Przychodnia.html',dane)

def Zapis(request):
    wszystko = Zapisy.objects.all()
    dane = {'wszystko': wszystko}
    return render(request,'Zapis.html',dane)

def Kontakt(request):
    return render(request,'Kontakt.html')

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()


    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
