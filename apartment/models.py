from django.db import models
from seller.models import Seller
from user.models import User


class ZIP(models.Model):
    zip = models.IntegerField(default=0, primary_key=True)
    city = models.CharField(max_length=999)

    def __str__(self):
        return '%s %s' % (self.zip, self.city)


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
    owner_ssn = models.BigIntegerField()
    owner_phone = models.IntegerField()
    sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.address


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.apartment


class ApartmentSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    size_from = models.IntegerField(null=True, blank=True)
    size_to = models.IntegerField(null=True, blank=True)
    price_from = models.IntegerField(null=True, blank=True)
    price_to = models.IntegerField(null=True, blank=True)
    rooms_from = models.IntegerField(null=True, blank=True)
    rooms_to = models.IntegerField(null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.address) + ' ' + str(self.number) + ' ' + str(self.zip) + ' ' + str(self.category)
