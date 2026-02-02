from django.db import models
from django.conf import settings

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    # Add other fields
