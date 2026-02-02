from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.accounts.managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    EMPLOYER = 'employer'
    JOBSEEKER = 'jobseeker'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EMPLOYER, 'Employer'),
        (JOBSEEKER, 'Jobseeker'),
    ]

    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_2fa_enabled = models.BooleanField(default=False)
    last_otp_verified_at = models.DateTimeField(null=True, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
            models.Index(fields=['role']),
            models.Index(fields=['date_joined']),
            models.Index(fields=['updated_at']),
        ]

    def __str__(self):
        return self.email or self.phone or str(self.id)

    def mark_otp_verified(self):
        self.last_otp_verified_at = timezone.now()
        self.save(update_fields=['last_otp_verified_at'])

    
    
   
    


    
