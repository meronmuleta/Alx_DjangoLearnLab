from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

 

class RegisterSerializer(serializers.ModelSerializer):
    # Add fields for password and token creation
    password = serializers.CharField()
    token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers', 'token']
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password in the API responses
        }

    # This method will create the user and generate a token
    def create(self, validated_data):
        # Create the user using the create_user method
        user = get_user_model().objects.create_user(
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

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers_count', 'following_count']