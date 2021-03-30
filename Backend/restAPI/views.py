from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("pk")
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated, ]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("pk")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, ]

