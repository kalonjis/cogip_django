from django.db import models
from django.template.defaultfilters import slugify

from office.countries import COUNTRIES

"""Company
    -name,
    -num tva,
    -type (provider or client),
    -invoices,
    -contacts
    """


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

