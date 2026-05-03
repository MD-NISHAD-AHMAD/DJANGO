from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from .models import *

# from rest_framework.response import Response


def home (request):
    return render (request, 'index.html')

def student_create(request):
    if request.method=='POST':

        name = request.POST.get('name')
        age = request.POST.get('age')
        location = request.POST.get('location')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            name = name,
            age = age,
            location = location,
            email = email,
            course = course
        )

    return render(request, 'form.html')



