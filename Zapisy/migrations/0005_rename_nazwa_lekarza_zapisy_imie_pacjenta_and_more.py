# Generated by Django 4.1.2 on 2022-10-14 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0004_lekarze_specjalizacja'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zapisy',
            old_name='Nazwa_lekarza',
            new_name='Imie_pacjenta',
        ),
        migrations.RenameField(
            model_name='zapisy',
            old_name='Specjalizacja',
            new_name='Nazwisko_pacjenta',
        ),
    ]
