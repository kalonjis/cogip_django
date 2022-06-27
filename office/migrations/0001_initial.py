# Generated by Django 4.0.5 on 2022-06-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('vat_number', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(choices=[('Prov', 'Provider'), ('Cli', 'Client')], default='Prov', max_length=100)),
            ],
        ),
    ]