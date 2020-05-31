from django.contrib import admin

from teacher.models import Teacher


class TeacherAdminModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


admin.site.register(Teacher, TeacherAdminModel)
