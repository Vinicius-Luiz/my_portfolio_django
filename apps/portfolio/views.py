from django.shortcuts import render
from apps.portfolio.models import About, Project, Skill
from apps.portfolio.functions import is_mobile

def index(request):
    abouts = About.objects.all()
    projects = Project.objects.all().filter(published = True).order_by("-developed_at")
    skills = Skill.objects.filter(published = True)
    mobile = is_mobile(request)
    return render(request, 'portfolio\index.html', {'abouts': abouts, 'projects': projects, 'skills': skills, 'is_mobile': mobile})
