from django.urls import path
from .views.auth import LoginView
from .views.profile import ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
