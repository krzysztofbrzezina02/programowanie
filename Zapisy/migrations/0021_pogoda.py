# Generated by Django 4.1.2 on 2022-10-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0020_formularz_kontaktowy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pogoda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pogodaa', models.CharField(max_length=60)),
            ],
        ),
    ]