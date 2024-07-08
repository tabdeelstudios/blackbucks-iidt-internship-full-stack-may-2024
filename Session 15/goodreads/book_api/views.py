from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User

from .models import Book
from .serializers import BookSerializer, UserSerializer

class BookView(generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request):
        allBooks = Book.objects.all()
        serilazedBooks = self.serializer_class(allBooks, many=True)
        return Response({"books":serilazedBooks.data})

class UserCreate(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer