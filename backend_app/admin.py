from django.contrib import admin

# Register your models here.
from .models import SensorData

# Register your models here.

Models = [SensorData]
for model in Models:
    admin.site.register(model)