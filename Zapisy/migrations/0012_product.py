# Generated by Django 4.1.2 on 2022-10-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapisy', '0011_lekarze_specjalizacja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('descripton', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
    ]
