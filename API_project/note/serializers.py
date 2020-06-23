from rest_framework import serializers
from .models import NoteModel

class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'author',
            'title',
            'body',
            'date',
        )
        
        model = NoteModel