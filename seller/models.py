from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1999, blank=True)
    year_of_start = models.DateTimeField()

    def __str__(self):
        return self.name


class SellerImage(models.Model):
    image = models.CharField(max_length=999)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
