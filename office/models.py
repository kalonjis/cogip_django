from django.db import models
from django.template.defaultfilters import slugify

from office.countries import COUNTRIES


class Company(models.Model):
    # Type of company choices
    CHOICES = (
        ('Prov', 'Provider'),
        ('Cli', 'Client')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    vat_number = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, choices=CHOICES, default='Prov')
    country = models.CharField(max_length=100, choices=COUNTRIES, blank=True)

    class Meta:
        verbose_name = "Compagnie"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name = "Contact"

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
            super().save(*args, **kwargs)


class Invoice(models.Model):
    increment_num = 1
    number = models.CharField(max_length=100, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def save(self, *args, increment_num=increment_num, **kwargs):
        if not self.number:
            self.number = str(increment_num).rjust(3, '0')
            Invoice.increment_num += 1
            super().save(*args, **kwargs)

