from rest_framework import serializers
from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for the User model.
    Converts User model instances into JSON representation for API consumption.
    """
    class Meta:
        model = User
        # Include fields consistent with the custom User model definition
        fields = ('id', 'email', 'phone', 'role', 'is_active', 'date_joined')
        read_only_fields = ('id', 'date_joined')
