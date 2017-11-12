from django.db import models

from .driver import Driver

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=30, default='')
    model = models.CharField(max_length=30, default='')
    number = models.CharField(max_length=20, default='')
    max_weight = models.IntegerField(null=True)
    max_volume = models.IntegerField(null=True)
    is_broken = models.BooleanField(default=False)
    driver = models.OneToOneField(Driver, default=None)

    def __str__(self):
        return self.number
