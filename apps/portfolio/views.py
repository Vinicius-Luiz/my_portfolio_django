from django.shortcuts import render
from apps.portfolio.models import About

def index(request):
    about = About.objects.all()
    return render(request, 'portfolio\index.html', {'abouts': about})
