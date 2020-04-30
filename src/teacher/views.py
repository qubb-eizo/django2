from .models import Teacher
from django.http import HttpResponse


def generate_teacher(request):
    for _ in range(15):
        Teacher.generate_teacher()
    abc = Teacher.objects.all()
    return HttpResponse(abc)
