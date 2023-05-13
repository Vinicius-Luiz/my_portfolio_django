from django.urls import path
from apps.portfolio.views import index

urlpatterns = [
    path('', index)
]