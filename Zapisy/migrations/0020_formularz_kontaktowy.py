# Generated by Django 4.1.2 on 2022-10-21 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0019_remove_zapisy_pacjent_specjalizacja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formularz_kontaktowy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=60, null=True)),
                ('Nazwisko', models.CharField(max_length=60, null=True)),
                ('Email', models.EmailField(max_length=60)),
                ('Opis', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
