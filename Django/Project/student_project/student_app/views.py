from django.shortcuts import render, redirect
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer


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



@api_view(['POST'])
def create_student(request):
    
    student = Student.objects.create(
        name=request.data.get('name'),
        age=request.data.get('age'),
        location=request.data.get('location'),
        email=request.data.get('email'),
        course=request.data.get('course')
    )

    
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['GET'])
def get_student(request, student_id):
    try:
        
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def update_student(request, student_id):
    try:

        student = Student.objects.get(student_id=student_id)

    except Student.DoesNotExist:
        return Response({'error': 'student not found'})
    
    serializer = StudentSerializer(student, data=request.data)


    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    
    return Response(serializer.errors)