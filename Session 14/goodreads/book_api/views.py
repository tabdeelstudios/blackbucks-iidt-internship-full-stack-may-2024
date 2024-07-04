from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Book
from .serializers import BookSerializer

class BookView(generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request):
        allBooks = Book.objects.all()
        serilazedBooks = self.serializer_class(allBooks, many=True)
        return Response({"books":serilazedBooks.data})
