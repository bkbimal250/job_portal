from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
