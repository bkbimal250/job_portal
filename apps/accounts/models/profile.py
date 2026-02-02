from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_index=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add other fields like avatar, phone Number etc
