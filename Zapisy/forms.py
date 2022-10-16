from django import forms
from .models import Zapisy_Pacjent

class ZapisyForm(forms.ModelForm):
    class Meta:
        model = Zapisy_Pacjent
        fields = [
        'Imie_pacjent',
        'Nazwisko_pacjent',
        'Wybor_lekarza',
        'Czas',
        ]

