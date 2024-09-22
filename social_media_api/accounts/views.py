from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework  import permissions, generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from .models import CustomUser


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Use the RegisterSerializer to validate and create a user
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This will also create a token for the user
            return Response(
                {"message": "User registered successfully", "token": serializer.data['token']}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # Retrieve or create the token for the user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserFollowView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response({"detail": "You cannot follow yourself."}, status=400)
            request.user.following.add(user_to_follow)
            return Response({"detail": f"You are now following {user_to_follow.username}."})
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)

class UserUnfollowView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."})
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)