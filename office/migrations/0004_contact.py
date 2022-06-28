# Generated by Django 4.0.5 on 2022-06-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_alter_company_options_alter_company_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
    ]
