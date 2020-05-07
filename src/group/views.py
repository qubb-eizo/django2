from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from group.forms import GroupAddForm
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

    result = '<br>'.join(str(group) for group in qsg)

    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': result}
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
        context={'form': form}
    )
