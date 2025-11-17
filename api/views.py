# api/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Profile, Author, Book
from .serializers import StudentSerializer, RegisterSerializer, UserSerializer, ProfileSerializer, AuthorSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .pagination import StudentPagination

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    filterset_fields = ['department', 'age']
    search_fields = ['name']
    ordering_fields = ['name', 'age']

def post(self, request):
    print("Request Data: ", request.data)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        print("DEBUG: Incoming Data ->", request.data)  # DEBUG

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print("DEBUG: Serializer Errors ->", serializer.errors)  # DEBUG
            return Response(serializer.errors, status=400)

        self.perform_create(serializer)

        print("DEBUG: Response data ->", serializer.data)  # DEBUG

        return Response(
            {"message": "User registered successfully", "user": serializer.data},
            status=201
        )


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        print("DEBUG: Auth User ->", self.request.user)  # DEBUG
        return self.request.user
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer