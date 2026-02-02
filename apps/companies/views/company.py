from rest_framework import viewsets
from ..models.company import Company
from ..serializers.company import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
