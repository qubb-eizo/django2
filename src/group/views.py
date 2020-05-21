from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from group.forms import GroupAddForm, GroupEditForm, GroupDeleteForm
from group.models import Group


def generate_group(request):
    for _ in range(15):
        Group.generate_group()
    abc = Group.objects.all()
    return HttpResponse(abc)


def groups_list(request):
    qsg = Group.objects.all()

    if request.GET.get('gname') or request.GET.get('gnum'):
        qsg = qsg.filter(Q(group_name=request.GET.get('gname')) | Q(
            group_number=request.GET.get('gnum')))

    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': qsg,
                 'title': 'Groups list'
                 }
    )


def groups_add(request):
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))

    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name='groups_add.html',
        context={'form': form,
                 'title': 'Groups add'
                 }
    )


def groups_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'group with id={id} does not exist')

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupEditForm(
            instance=group
        )

    return render(
        request=request,
        template_name='groups_edit.html',
        context={
            'form': form,
            'title': 'Groups edit',
            'group': group
        }
    )


def groups_delete(request, id):
    try:
        student = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'group with id={id} does not exist')

    if request.method == 'POST':
        form = GroupDeleteForm(request.POST, instance=student)
        student.delete()
        if form.is_valid():
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupDeleteForm(instance=student)

    return render(
        request=request,
        template_name='groups_delete.html',
        context={
            'form': form,
            'title': 'Group delete'
        },
    )
