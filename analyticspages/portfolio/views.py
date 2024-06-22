from django.shortcuts import render, get_object_or_404
from .models import Project

# Function-based view to display a list of all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

# Function-based view to display the details of a specific project
def project_list(request, pk):
    projects = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'projects': projects})