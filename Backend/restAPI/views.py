from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HumanSerializer
from .models import Human


class HumanViewSet(viewsets.ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all().order_by("pk")

