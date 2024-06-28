from rest_framework import serializers
from .models import NoteModel

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = '__all__'