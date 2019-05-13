from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
#from apartment.models import Apartment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Sale(models.Model):
    date = models.DateTimeField(blank=True)
    cardholder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card_num_1 = models.DecimalField(max_digits=4, decimal_places=0)
    card_num_2 = models.DecimalField(max_digits=4, decimal_places=0)
    card_num_3 = models.DecimalField(max_digits=4, decimal_places=0)
    card_num_4 = models.DecimalField(max_digits=4, decimal_places=0)
    cvc = models.DecimalField(max_digits=3, decimal_places=0)
    expire = models.DateField()
