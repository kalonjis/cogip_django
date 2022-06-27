# Generated by Django 4.0.5 on 2022-06-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_company_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Compagnie'},
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, unique=True),
        ),
    ]
