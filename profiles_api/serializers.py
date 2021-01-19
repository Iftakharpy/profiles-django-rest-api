from rest_framework import serializers
from .models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""
    name = serializers.CharField(max_length=255)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes UserProfile model"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and Return a user from provided data."""
        user = UserProfile.objects.create_user(
            email = validated_data.get('email'),
            name = validated_data.get('name'),
            password = validated_data.get('password')
        )

        return user


