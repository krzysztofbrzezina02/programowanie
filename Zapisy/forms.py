from django import forms
from .models import Zapisy_Pacjent
from .models import Formularz_kontaktowy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
class ZapisyForm(forms.ModelForm):
    class Meta:
        model = Zapisy_Pacjent
        fields = [
        'Imie_pacjent',
        'Nazwisko_pacjent',
        'Wybor_lekarza',
        'Data',
        ]


class FormularzForm(forms.ModelForm):
    class Meta:
        model = Formularz_kontaktowy
        fields = [
        'Imie',
        'Nazwisko',
        'Email',
        'Opis',
        ]

#class Zapisy_ulepszenie(forms.Form):
    #Imie = forms.CharField(required=True,label = 'Imie',max_length=32)
    #Nazwisko = forms.CharField(required=True,label = 'Nazwisko',max_length=32)
    #Lekarz = forms.CharField(required=True,label = 'Lekarz',max_length=32)
    #data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    #czas = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'time'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'password1',
        'password2',
        ]
