from django.http import HttpResponse
from django.shortcuts import render
from group.models import Group


def generate_group(request):
    for _ in range(15):
        Group.generate_group()
    abc = Group.objects.all()
    return HttpResponse(abc)


def groups_list(request):
    qsg = Group.objects.all()

    if request.GET.get('gname'):
        qsg = qsg.filter(group_name=request.GET.get('gname'))

    if request.GET.get('gnum'):
        qsg = qsg.filter(group_number=request.GET.get('gnum'))

    result = '<br>'.join(
        str(group)
        for group in qsg
    )

    return render(
        request=request,
        template_name='groups_list.html',
        context={'groups_list': result}
    )
