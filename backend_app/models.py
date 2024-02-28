from django.db import models

class SensorData(models.Model):
    created_at = models.DateTimeField(primary_key=True)
    entry_id = models.IntegerField(null=True, blank=True)
    field1 = models.IntegerField(null=True, blank=True)
    field2 = models.FloatField(null=True, blank=True)
    field3 = models.FloatField(null=True, blank=True)
    field4 = models.FloatField(null=True, blank=True)