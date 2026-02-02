from django.db import models
from django.conf import settings

class Application(models.Model):
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
