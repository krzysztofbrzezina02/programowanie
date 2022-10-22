# Generated by Django 4.1.2 on 2022-10-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0022_alter_formularz_kontaktowy_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktualnosci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacja', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Aktualnosci',
                'verbose_name_plural': 'Aktualnosci',
            },
        ),
        migrations.DeleteModel(
            name='Pogoda',
        ),
    ]