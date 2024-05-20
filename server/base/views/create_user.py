from django.contrib.auth.models import User
from rest_framework import generics
from ..serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..permissions import IsTeacher

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
