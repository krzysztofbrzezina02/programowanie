# Generated by Django 4.1.3 on 2022-12-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0032_alter_zapisy_pacjent_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapisy_pacjent',
            name='Data',
            field=models.DateField(blank=True, null=True, verbose_name=['%d-%m-%Y']),
        ),
    ]
