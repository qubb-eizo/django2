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
from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url
from teacher.views import teachers_list, generate_teachers, teachers_add, teachers_edit, teachers_delete
from student.views import students_list, generate_students, students_add, students_edit, students_delete
from group.views import groups_list, generate_group, groups_add, groups_edit, groups_delete

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
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
        path('groups/add/', groups_add, name='groups-add'),
        path('students/edit/<int:id>', students_edit, name='students-edit'),
        path('students/delete/<int:id>', students_delete, name='students-delete'),
        path('teachers/edit/<int:id>', teachers_edit, name='teachers-edit'),
        path('groups/edit/<int:id>', groups_edit, name='groups-edit'),
        path('teachers/delete/<int:id>', teachers_delete, name='teachers-delete'),
        path('groups/delete/<int:id>', groups_delete, name='groups-delete')
    ]
