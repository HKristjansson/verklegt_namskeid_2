from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=2999, blank=True)
    year_of_start = models.DateTimeField()
    disabled = models.BooleanField()

    def __str__(self):
        return self.name


class SellerImage(models.Model):
    image = models.CharField(max_length=2999)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
