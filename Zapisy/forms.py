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

#class UserRegistrationForm(forms.Form):
    #username = forms.CharField(required=True,label = 'Username',max_length=32)
    #email = forms.CharField(required=True,label = 'Email',max_length=32)
   # password = forms.CharField(required=True,label = 'Password',max_length=32)
   # data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))

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
