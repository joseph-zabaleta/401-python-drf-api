# from django.shortcuts import render
from .models import NoteModel
# from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import NoteSerializer

class NoteListView(generics.ListCreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
