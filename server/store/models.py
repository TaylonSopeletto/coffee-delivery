from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    taxNumber = models.TextField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.taxNumber

class Address(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    street = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    number = models.CharField(max_length=100, blank=True, default='')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    def __str__(self):
        return self.name


class Coffee(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Order(models.Model):
    
    products = models.ManyToManyField(Coffee)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def total_price(self):
        queryset = self.products.all().aggregate(
        total_price=models.Sum('price'))
        return queryset["total_price"]
    
    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


