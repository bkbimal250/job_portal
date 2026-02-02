from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
