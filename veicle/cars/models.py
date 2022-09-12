from django.db import models

# Create your models here.
class Auto(models.Model):
    title = models.CharField(max_length=20)
    speed = models.FloatField()
    description = models.TextField()
    year_create = models.IntegerField()
    def __str__(self):
        return  self.title