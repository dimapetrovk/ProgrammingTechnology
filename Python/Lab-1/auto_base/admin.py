from django.contrib import admin

from .models import *

admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(Trip)
admin.site.register(Car)