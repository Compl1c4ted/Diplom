from django.urls import path
from . import views

urlpatterns = [
    path('project_list', views.view_projects, name='projects'),
]
