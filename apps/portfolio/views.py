from django.shortcuts import render
from apps.portfolio.models import About, Project, Skill

def index(request):
    abouts = About.objects.all()
    projects = Project.objects.all().filter(published = True).order_by("-developed_at")
    skills = Skill.objects.filter(published = True)
    return render(request, 'portfolio\index.html', {'abouts': abouts, 'projects': projects, 'skills': skills})
