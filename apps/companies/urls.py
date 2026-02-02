from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.company import CompanyViewSet

router = DefaultRouter()
router.register(r'', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
