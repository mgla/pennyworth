from django.db import models

class Action(models.Model):
    label = models.CharField(max_length=200)

class Device(models.Model):
    mac   = models.IntegerField()
    label = models.CharField(max_length=200)
    def __str__(self):
        return "%s with MAC address '%X'" % (self.label, self.mac)
