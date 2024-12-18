from django.db import models
from django.utils import timezone
from projects.models import Project


class Tasks(models.Model):
    title = models.CharField(max_length=55)
    descriptions = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    TODO = 'todo'
    IN_PROCESS = 'in_process'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROCESS, 'In Process'),
        (COMPLETED, 'Completed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TODO,
        )
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_status_color(self):
        """Возвращает цвет для статуса задачи."""
        if self.status == self.TODO:
            return 'bg-gray-200 text-gray-800'
        elif self.status == self.IN_PROCESS:
            return 'bg-yellow-200 text-yellow-800'
        elif self.status == self.COMPLETED:
            return 'bg-green-200 text-green-800'
        return 'bg-gray-200 text-gray-800'
