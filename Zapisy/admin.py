from django.contrib import admin

from .models import Specjalizacje,Lekarze,Zapisy_Pacjent


# Register your models here.

#admin.site.register(Zapisy)
admin.site.register(Specjalizacje)
admin.site.register(Lekarze)
admin.site.register(Zapisy_Pacjent)
