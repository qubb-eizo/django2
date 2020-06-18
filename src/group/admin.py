from django.contrib import admin

from group.models import Group, Classroom
from student.models import Student


class StudentsInline(admin.TabularInline):
    model = Student
    readonly_fields = ('birthdate', 'last_name', 'first_name', 'email')
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    fields = ['group_name', 'classroom']
    inlines = (StudentsInline,)
    list_per_page = 10


admin.site.register(Group, GroupAdmin)
