from django.shortcuts import render
from .models import Project

def home(requst):
    projects = Project.objects.all()
    return render(requst, 'portfolio/home.html', {'projects': projects})
