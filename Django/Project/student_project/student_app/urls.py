from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('create/', views.student_create, name='student_create'),
    # path('studentlist/', views.student_list, name='student_list'),
    # path('student/update/<int:student_id>/', views.student_update, name='student_update'),
    # path('student/delete/<int:student_id>/', views.student_delete, name='student_delete'),
       

           # get all students
     path('api/students/create/', views.create_student, name='create_student'),

    # post create student 
     path('api/student/<int:student_id>/', views.get_student, name='get_student'),

     # update 
       path('api/student/update/<int:student_id>/', views.update_student, name='update_student'),
]
