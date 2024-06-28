from rest_framework.response import Response
from rest_framework import status, generics
from datetime import datetime
from .models import NoteModel
from .serializers import NoteSerializer

class NoteView(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get(self, request):
        notes = NoteModel.objects.all()
        serializer = self.serializer_class(notes, many=True)
        return Response({
            "notes":serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":{"note":serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"failed", "data":{"messages":serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)
        
class NoteDetail(generics.GenericAPIView):
    serializer_class = NoteSerializer
    queryset = NoteModel.objects.all()

    def get_note(self, pk):
        try:
            return NoteModel.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk):
        note = self.get_note(pk=pk)
        if note==None:
            return Response({"status":"failed", f"message":"Note with ID:{pk} not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.serializer_class(note)
            return Response({"status":"success", "data":{"note":serializer.data}}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        note = self.get_note(pk=pk)
        if note==None:
            return Response({"status":"failed", f"message":"Note with ID:{pk} not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt']=datetime.now()
            serializer.save()
            return Response({"status":"success", "data":{"note":serializer.data}}, status=status.HTTP_200_OK)
        
        return Response({"status":"failed", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_note(pk=pk)
        if note==None:
            return Response({"status":"failed", f"message":"Note with ID:{pk} not found"}, status=status.HTTP_400_BAD_REQUEST)

        note.delete()
        return Response({"status":"deleted"}, status=status.HTTP_204_NO_CONTENT)