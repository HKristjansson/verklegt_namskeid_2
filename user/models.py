from django.db import models


# Create your models here.
class User(models.model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    b_day = models.DateField
    search_history = models.CharField(max_length=255)
    is_employee = models.BooleanField(bool=False)
