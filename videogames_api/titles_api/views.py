from django.shortcuts import render


# Create your views here.
from rest_framework import generics
from .serializers import TitleSerializer
from .models import Title

class TitleList(generics.ListCreateAPIView):
    queryset = Title.objects.all().order_by('id')
    serializer_class = TitleSerializer

class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all().order_by('id')
    serializer_class = TitleSerializer