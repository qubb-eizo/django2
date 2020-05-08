from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from teacher.models import Teacher
from teacher.forms import TeacherAddForm


def generate_teachers(request):
    for _ in range(10):
        Teacher.generate_teacher()
    abc = Teacher.objects.all()
    return HttpResponse(abc)


def teachers_list(request):
    qsg = Teacher.objects.all()

    if request.GET.get('tfname') or request.GET.get('tlname') or request.GET.get('email'):
        qsg = qsg.filter(Q(first_name=request.GET.get('tfname')) | Q(
            last_name=request.GET.get('tlname')) | Q(email=request.GET.get('email')))

    result = '<br>'.join(str(group) for group in qsg)

    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': result}
    )


def teachers_add(request):
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))

    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teachers_add.html',
        context={'form': form}
    )