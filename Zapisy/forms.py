from django import forms
from .models import Product

class ZapisyForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        'Imie_pacjent',
        'Nazwisko_pacjent',
        'Wybor_lekarza',
        'Czas',
        ]

