from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Handles the validation of credentials during the authentication process.
    """
    # Use email as the primary identifier (consistent with User model USERNAME_FIELD)
    email = serializers.EmailField()
    
    # Password field, marked as write_only to ensure it's not included in response data
    password = serializers.CharField(write_only=True)
