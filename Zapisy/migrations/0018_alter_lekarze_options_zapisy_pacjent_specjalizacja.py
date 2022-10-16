# Generated by Django 4.1.2 on 2022-10-16 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0017_alter_lekarze_options_delete_zapisy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lekarze',
            options={'verbose_name': 'Lekarz', 'verbose_name_plural': 'Lekarze'},
        ),
        migrations.AddField(
            model_name='zapisy_pacjent',
            name='specjalizacja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Zapisy.specjalizacje'),
        ),
    ]
