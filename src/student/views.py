from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from student.forms import StudentAddForm, StudentEditForm, StudentDeleteForm
from student.models import Student


def generate_students(request):
    for _ in range(15):
        Student.generate_student()
    abc = Student.objects.all()
    return HttpResponse(abc)


def students_list(request):
    qs = Student.objects.all().select_related('group')

    if request.GET.get('fname') or request.GET.get('lname') or request.GET.get('email'):
        qs = qs.filter(Q(first_name=request.GET.get('fname')) | Q(
            last_name=request.GET.get('lname')) | Q(email=request.GET.get('email')))

    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': qs,
                 'title': 'Students list'
                 }
    )


def students_add(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={
            'form': form,
            'title': 'Students add'
        }
    )


def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'student with id={id} does not exist')

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_edit.html',
        context={
            'form': form,
            'title': 'Student edit',
            'student': student
        },
    )


def students_delete(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'student with id={id} does not exist')

    if request.method == 'POST':
        form = StudentDeleteForm(request.POST, instance=student)
        student.delete()
        if form.is_valid():
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentDeleteForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_delete.html',
        context={
            'form': form,
            'title': 'Student delete'
        },
    )
