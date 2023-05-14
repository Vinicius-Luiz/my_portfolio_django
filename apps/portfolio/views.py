from django.shortcuts import render
from apps.portfolio.models import About, Project, Skill
from apps.portfolio.functions import is_mobile
from apps.portfolio.utils import project_type_button, skill_type_button

def index(request):
    abouts = About.objects.all()

    if 'project' not in request.GET or request.GET['project'] == 'ALL':
        projects = Project.objects.all().filter(published = True).order_by("-developed_at")
    else:
        project = request.GET['project']
        projects = Project.objects.all().filter(published = True, type = project).order_by("-developed_at")
    
    if 'skill' not in request.GET or request.GET['skill'] == 'ALL':
        skills = Skill.objects.filter(published = True)
    else:
        skill = request.GET['skill']
        skills = Skill.objects.filter(published = True, type = skill)


    project_choices = list()
    for key, type_display in Project.PROJECT_TYPE:
        project_choices.append((key, type_display, project_type_button[key]))
    
    skill_choices = list()
    for key, type_display in Skill.SKILL_TYPE:
        skill_choices.append((key, type_display, skill_type_button[key]))

    mobile = is_mobile(request)

    data = {
          'abouts': abouts
        , 'projects': projects
        , 'skills': skills
        , 'is_mobile': mobile
        , 'project_choices': project_choices
        , 'skill_choices': skill_choices
    }
    return render(request, 'portfolio\index.html', data)
