from rest_framework import viewsets
from ..models.application import Application
from ..serializers.application import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
