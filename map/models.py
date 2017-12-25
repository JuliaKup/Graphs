from django.db import models

# Create your models here.

max_length = 200


class Station(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=max_length, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    zone = models.IntegerField(null=False)
    total_lines = models.IntegerField(null=False)
    rail = models.IntegerField(null=False)


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    rid = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=max_length, null=False)
    colour = models.CharField(max_length=max_length, null=False)
    stripe = models.CharField(max_length=max_length, null=True)


class Line(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    station1 = models.ForeignKey(Station, related_name='station1')
    station2 = models.ForeignKey(Station, related_name='station2')
    route_id = models.ForeignKey(Route)
    time = models.IntegerField()