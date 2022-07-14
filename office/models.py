from django.contrib.auth import apps
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

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
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def type_value(self):
        return self.get_type_display()

    @property
    def country_value(self):
        return self.get_country_display()

    def get_absolute_url(self):
        return reverse('office:company-detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Contact"

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('office:contact-detail', kwargs={'slug': self.slug})


class Invoice(models.Model):
    increment_num = 2
    number = models.CharField(max_length=100, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = str(Invoice.increment_num).rjust(3, '0')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('office:invoice-detail', kwargs={'pk': self.pk})


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Vous devez rentrer un nom d'utilisateur")
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
