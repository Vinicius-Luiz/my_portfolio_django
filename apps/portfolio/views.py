from django.shortcuts import render
from apps.portfolio.models import About, Project

def index(request):
    abouts = About.objects.all()
    projects = Project.objects.all().order_by("-developed_at")
    return render(request, 'portfolio\index.html', {'abouts': abouts, 'projects': projects})
