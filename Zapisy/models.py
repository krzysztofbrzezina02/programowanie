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

class Zapisy(models.Model):
    def __str__(self):
        return self.Nazwisko_pacjenta

    Imie_pacjenta = models.CharField(max_length=60)
    Nazwisko_pacjenta = models.CharField(max_length=60)
    Wybor_lekarza = models.ForeignKey(Lekarze,on_delete=models.CASCADE,null=True)
    Czas = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    class Meta:
        verbose_name = "Zapisy"
        verbose_name_plural = "Zapisy"

class Product(models.Model):

    #title = models.CharField(max_length=60)
    #descripton = models.TextField(blank=True,null=True)
    #price = models.DecimalField(default=False,decimal_places=2, max_digits = 10000)
    Imie_pacjent = models.CharField(max_length=60,null=True)
    Nazwisko_pacjent = models.CharField(max_length=60,null=True)
    Wybor_lekarza = models.ForeignKey(Lekarze,on_delete=models.CASCADE,null=True)
    Czas = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True ,null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"

    def __str__(self):
        return self.Nazwisko_pacjent





