from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics

from .models import NoteModel
from .serializers import NoteSerializer

class Notes(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self, request):
        notes = NoteModel.objects.all()
        serializer = self.serializer_class(notes, many=True)
        return Response({
            "notes":serializer.data, "message":"This is response"
        })



