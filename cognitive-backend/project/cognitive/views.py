from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import CognitiveModel

# Create your views here.


class CognitiveView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = CognitiveModel.objects.all()
