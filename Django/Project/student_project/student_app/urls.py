from django.urls import path, include
from student_app import views as v

urlpatterns = [
    path('',v.home,name="home"),
    path('create' , v.student_create, name ="student_create"),
   ]