from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AreaSerializer
from .models import Area


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()