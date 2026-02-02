# apps/accounts/models/profile.py

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='%(class)s')

    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='profile/avatars/', null=True, blank=True)

    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='India')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class JobSeekerProfile(BaseProfile):
    NOTICE_PERIOD_CHOICES = [
        ('IMMEDIATE', 'Immediate'),
        ('15_DAYS', '15 Days'),
        ('1_MONTH', '1 Month'),
        ('2_MONTHS', '2 Months'),
        ('3_MONTHS', '3 Months'),
    ]

    headline = models.CharField(max_length=255, blank=True)
    experience_years = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    skills = models.TextField(blank=True, help_text="Comma separated skills")
    
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    current_salary = models.PositiveIntegerField(null=True, blank=True)
    expected_salary = models.PositiveIntegerField(null=True, blank=True)
    notice_period = models.CharField(max_length=20, choices=NOTICE_PERIOD_CHOICES, default='1_MONTH')
    
    preferred_locations = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)
    
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    class Meta:
        db_table = 'jobseeker_profiles'

    def __str__(self):
        return f"JobSeeker: {self.full_name}"


class EmployerProfile(BaseProfile):
    COMPANY_SIZE_CHOICES = [
        ('1-10', '1-10 Employees'),
        ('11-50', '11-50 Employees'),
        ('51-200', '51-200 Employees'),
        ('201-500', '201-500 Employees'),
        ('501-1000', '501-1000 Employees'),
        ('1000+', '1000+ Employees'),
    ]

    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    company_size = models.CharField(max_length=20, choices=COMPANY_SIZE_CHOICES, blank=True)
    
    office_address = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)

    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'employer_profiles'

    def __str__(self):
        return f"Employer: {self.company_name}"
