from django.db import models
from users.models import User


class Project(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # status = ...
    # importance = ...
