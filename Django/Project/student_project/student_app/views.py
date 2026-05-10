from django.shortcuts import render, redirect
from .models import Student


def home(request):
    return render(request, 'index.html')


def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            location=request.POST.get('location'),
            email=request.POST.get('email'),
            course=request.POST.get('course')
        )
        return redirect('student_list')

    return render(request, 'form.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_update(request, student_id):
    student = Student.objects.filter(student_id=student_id).first()

    if request.method == 'POST':
        Student.objects.filter(student_id=student_id).update(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            location=request.POST.get('location'),
            email=request.POST.get('email'),
            course=request.POST.get('course')
        )
        return redirect('student_list')

    return render(request, 'form.html', {'student': student})


def student_delete(request, student_id):
    Student.objects.filter(student_id=student_id).delete()
    return redirect('student_list')