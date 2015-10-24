from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class Session(models.Model):
    event = models.ForeignKey(Event)
    date = models.DateField()


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Result(models.Model):
    session = models.ForeignKey(Session)
    player = models.ForeignKey(Player)
    points = models.IntegerField(blank=True)
