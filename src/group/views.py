from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from group.forms import GroupAddForm, GroupEditForm
from group.models import Group


def generate_group(request):
    for _ in range(15):
        Group.generate_group()
    abc = Group.objects.all()
    return HttpResponse(abc)


class GroupsListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'
    login_url = reverse_lazy('user_account:login')
    paginate_by = 3

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


class GroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'groups_edit.html'
    form_class = GroupEditForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('groups:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit group'
        return context


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'students_add.html'
    form_class = GroupAddForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupsDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups_delete.html'
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('groups:list')
