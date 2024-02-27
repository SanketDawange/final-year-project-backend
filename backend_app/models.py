from django.db import models

class SensorData(models.Model):
    created_at = models.DateTimeField(primary_key=True)
    entry_id = models.IntegerField()
    field1 = models.IntegerField()
    field2 = models.FloatField()
    field3 = models.FloatField()
    field4 = models.FloatField(null=True, blank=True)