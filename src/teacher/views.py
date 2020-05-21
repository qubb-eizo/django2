from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from teacher.models import Teacher
from teacher.forms import TeacherAddForm, TeacherEditForm, TeacherDeleteForm


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

    return render(
        request=request,
        template_name='teachers_list.html',
        context={'teachers_list': qsg,
                 'title': 'Teachers list'
                 }
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
        context={'form': form,
                 'title': 'Teachers add'
                 }
    )


def teachers_edit(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'teacher with id={id} does not exist')

    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherEditForm(
            instance=teacher
        )

    return render(
        request=request,
        template_name='teachers_edit.html',
        context={
            'form': form,
            'title': 'Teachers edit',
            'teacher': teacher
        }
    )


def teachers_delete(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'teacher with id={id} does not exist')

    if request.method == 'POST':
        form = TeacherDeleteForm(request.POST, instance=teacher)
        teacher.delete()
        if form.is_valid():
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherDeleteForm(
            instance=teacher
        )

    return render(
        request=request,
        template_name='teachers_delete.html',
        context={
            'form': form,
            'title': 'Teacher delete'
        },
    )
