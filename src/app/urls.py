"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teacher.views import teachers_list, generate_teachers, teachers_add
from student.views import students_list, generate_students, students_add
from group.views import groups_list, generate_group, groups_add


urlpatterns = [
    path('admin/', admin.site.urls, name='admin-panel'),
    path('', admin.site.urls, name='admin-panel1'),
    path('teachers/', teachers_list, name='teachers'),
    path('students/', students_list, name='students'),
    path('groups/', groups_list, name='groups'),
    path('group-gen/', generate_group, name='groups-gen'),
    path('teacher-gen/', generate_teachers, name='teachers-gen'),
    path('student-gen/', generate_students, name='students-gen'),
    path('students/add/', students_add, name='students-add'),
    path('teachers/add/', teachers_add, name='teachers-add'),
    path('groups/add/', groups_add, name='groups-add')
]
