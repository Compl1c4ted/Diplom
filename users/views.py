from django.shortcuts import render
from .models import User


def index(request):
    user = User()
    return user
