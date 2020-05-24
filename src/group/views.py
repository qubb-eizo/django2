from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


def generate_group(request):
    for _ in range(15):
        Group.generate_group()
    abc = Group.objects.all()
    return HttpResponse(abc)


class GroupsListView(ListView):
    model = Group
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'

    def get_queryset(self):
        request = self.request
        qsg = super().get_queryset()

        if request.GET.get('gname') or request.GET.get('gnum'):
            qsg = qsg.filter(Q(group_name=request.GET.get('gname')) | Q(
                group_number=request.GET.get('gnum')))

        return qsg

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group list'
        return context


class GroupsUpdateView(UpdateView):
    model = Group
    template_name = 'groups_edit.html'
    form_class = GroupEditForm

    def get_success_url(self):
        return reverse('groups:list')


class GroupsCreateView(CreateView):
    model = Group
    template_name = 'students_add.html'
    form_class = GroupAddForm

    def get_success_url(self):
        return reverse('groups:list')


class GroupsDeleteView(DeleteView):
    model = Group
    template_name = 'groups_delete.html'

    def get_success_url(self):
        return reverse('groups:list')
