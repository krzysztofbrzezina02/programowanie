from django.contrib import admin

from .models import Zapisy,Specjalizacje,Lekarze,Product


# Register your models here.

admin.site.register(Zapisy)
admin.site.register(Specjalizacje)
admin.site.register(Lekarze)
admin.site.register(Product)
