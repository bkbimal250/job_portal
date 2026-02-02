from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
