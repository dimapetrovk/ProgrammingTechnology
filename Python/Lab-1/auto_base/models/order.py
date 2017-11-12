from django.db import models

from .car import Car
from .trip import Trip


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.OneToOneField(Car, default=None)
    trip = models.OneToOneField(Trip, default=None)
    payment = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.car) + " " + str(self.trip)
