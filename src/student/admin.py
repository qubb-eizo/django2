from django.contrib import admin

from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')

    def get_queryset(self, request):
        return super(StudentAdminModel, self).get_queryset(request).\
            select_related('group')


admin.site.register(Student, StudentAdminModel)
