from django.db import models
from seller.models import Seller

# Create your models here.


class ApartmentCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    zip = models.IntegerField()
    description = models.CharField(max_length=255)
    rooms = models.IntegerField()
    size = models.FloatField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(ApartmentCategory, on_delete=models.CASCADE, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True)
    owner_name = models.CharField(max_length=255)
    owner_ssn = models.IntegerField()
    owner_phone = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return self.address


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

