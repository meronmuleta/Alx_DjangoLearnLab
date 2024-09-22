from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Add fields for password and token creation
    password = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers', 'token']
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password in the API responses
        }

    # This method will create the user and generate a token
    def create(self, validated_data):
        # Create the user using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        
        # Create a token for the new user
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        # Retrieve the token for the user
        token = Token.objects.get(user=obj)
        return token.key
