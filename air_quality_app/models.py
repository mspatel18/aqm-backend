from django.db import models

class AirQualityData(models.Model):
    timestamp = models.DateTimeField()
    particulate_matter = models.FloatField()
    carbon_monoxide = models.FloatField()
    air_quality_index = models.FloatField()
    nitrogen_dioxide=models.FloatField()
