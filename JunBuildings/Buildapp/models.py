from django.contrib.gis.db import models


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField()
    address = models.CharField()
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')


# Returns the string representation of the model.
def __str__(self):
    return self.name
