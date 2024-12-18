from django.db import models


class User(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False)
    bio = models.TextField(null=True, blank=True)
    # avatar = models.ImageField()
    join_date = models.DateField(auto_now_add=True, blank=True)
