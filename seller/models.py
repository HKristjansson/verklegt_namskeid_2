from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=2999, blank=True)
    year_of_start = models.DateTimeField()
    disabled = models.BooleanField(default=False)
    description = models.CharField(max_length=1024)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name