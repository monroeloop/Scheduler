import datetime
from calendar import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def calendar_view(request):
    return render(request, 'pages/calendar_view.html', {})

def main(request):
    return render(request, 'pages/main.html', {})

@login_required
def new_login(request):
    members = Member.objects.all()

