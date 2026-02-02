from rest_framework import viewsets
from ..models.job import Job
from ..serializers.job import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
