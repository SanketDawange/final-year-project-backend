from django.contrib import admin

# Register your models here.
from .models import SensorData, Alert

# Register your models here.

Models = [SensorData, Alert]
for model in Models:
    admin.site.register(model)