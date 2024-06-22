from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request, pk):
    projects = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_list.html', {'projects': projects})