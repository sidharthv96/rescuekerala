from django.db import models

# Create your models here.
class Pickup(models.Model):
    name = models.CharField(max_length=50, blank=True)
    mobilenumber = models.IntegerField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    latt = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    medicalemergency = models.BooleanField(default=False, blank=True)
    medicalreason = models.TextField(blank=True)
    no_people = models.IntegerField(blank=True)

    def __str__(self):
        return(self.name)
