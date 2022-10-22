from django import forms
from .models import Zapisy_Pacjent
from .models import Formularz_kontaktowy

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

 #   class Meta:
  #      model = Rejestracja
   #     fields = [
    #    'username',
     #   'email',
      #  'password',
       # ]

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
