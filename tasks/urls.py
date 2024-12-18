from django.urls import path
from . import views

urlpatterns = [
    path('tasks_list', views.view_tasks, name='tasks'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('task_detail/<int:id>/', views.task_detail, name='task_detail'),
    
]
