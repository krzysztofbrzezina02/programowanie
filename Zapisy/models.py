from django.db import models


# Create your models here.
class Specjalizacje(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)

    class Meta:
       verbose_name = "Specjalizacja"
       verbose_name_plural = "Specjalizacje"

class Lekarze(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    specjalizacja = models.ForeignKey(Specjalizacje,on_delete=models.CASCADE,null=True)


    class Meta:
       verbose_name = "Lekarz"
       verbose_name_plural = "Lekarze"

class Zapisy_Pacjent(models.Model):

    Imie_pacjent = models.CharField(max_length=60,null=True)
    Nazwisko_pacjent = models.CharField(max_length=60,null=True)
    Wybor_lekarza = models.ForeignKey(Lekarze,on_delete=models.CASCADE,null=True)
    Data = models.DateTimeField(null=True,blank=True,auto_now_add=False)
    Czas = models.TimeField(null=True,auto_now_add=False)

    class Meta:
        verbose_name = "Zapisy_Pacjent"
        verbose_name_plural = "Zapisy_Pacjent"

    def __str__(self):
        return self.Nazwisko_pacjent


class Formularz_kontaktowy(models.Model):
    Imie = models.CharField(max_length=60, null=True)
    Nazwisko = models.CharField(max_length=60, null=True)
    Email = models.EmailField(max_length=60)
    Opis = models.TextField (max_length=200,null=True)

    class Meta:
        verbose_name = "Formularz_kontaktowy"
        verbose_name_plural = "Formularz_kontaktowy"




    def __str__(self):
        return self.Email

class Oceny_Lekarzy(models.Model):
    def __str__(self):
        return self.Ocena

    Wybor_lekarza = models.ForeignKey(Lekarze,on_delete=models.CASCADE,null=True)
    Ocena = models.CharField(max_length=60,null=True)

    class Meta:
       verbose_name = "Oceny"
       verbose_name_plural = "Oceny"








