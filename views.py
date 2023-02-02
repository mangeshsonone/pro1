from django.shortcuts import render

from rest_framework import viewsets
from .models import student
from .serializers import studentserializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class studata(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentserializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
