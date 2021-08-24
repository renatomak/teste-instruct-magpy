from rest_framework import viewsets
from django.shortcuts import render, redirect

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "name"


def Home(request):
    return render(request, 'index.html')
