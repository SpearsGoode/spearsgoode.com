from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    proj_list = Project.objects
    return render(request, 'projects/projects.html', {'projects': proj_list})
