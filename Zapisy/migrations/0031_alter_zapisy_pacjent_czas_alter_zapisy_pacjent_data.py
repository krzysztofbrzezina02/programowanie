# Generated by Django 4.1.3 on 2022-12-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0030_alter_zapisy_pacjent_czas_alter_zapisy_pacjent_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapisy_pacjent',
            name='Czas',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='zapisy_pacjent',
            name='Data',
            field=models.DateField(null=True),
        ),
    ]