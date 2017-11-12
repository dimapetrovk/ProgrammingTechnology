from django.db import models


class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    start_city = models.CharField(max_length=30, default='')
    end_city = models.CharField(max_length=30, default='')

    def __str__(self):
        return "From " + self.start_city + " to " + self.end_city
