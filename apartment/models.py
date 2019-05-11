from django.db import models
from seller.models import Seller


class ZIP(models.Model):
    zip = models.IntegerField(default=0, primary_key=True)
    city = models.CharField(max_length=999)

    def __str__(self):
        return str(self.zip) + ' ' + self.city


class ApartmentCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    zip = models.ForeignKey(ZIP, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=1524)
    rooms = models.IntegerField()
    size = models.FloatField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(ApartmentCategory, on_delete=models.CASCADE, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True)
    owner_name = models.CharField(max_length=255)
    owner_ssn = models.IntegerField()
    owner_phone = models.IntegerField()
    sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    buyer = models.CharField(max_lenght=30)

    def __str__(self):
        return self.address


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.apartment

