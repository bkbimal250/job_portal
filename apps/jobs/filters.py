import django_filters
from .models.job import Job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['title', 'company']
