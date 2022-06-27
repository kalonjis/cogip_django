from django.db import models

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
    slug = models.SlugField()
    vat_number = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, choices=CHOICES, default='Prov')
