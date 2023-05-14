from django.urls import path
from apps.portfolio.views import index

urlpatterns = [
    path('', index, name='index'),
    path('search_project', index, name='search_project'),
    path('search_skill', index, name='search_skill'),
]