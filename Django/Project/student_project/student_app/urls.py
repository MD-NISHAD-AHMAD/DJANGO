from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.student_create, name='student_create'),
    path('studentlist/', views.student_list, name='student_list'),
    path('student/update/<int:student_id>/', views.student_update, name='student_update'),
    path('student/delete/<int:student_id>/', views.student_delete, name='student_delete'),
]