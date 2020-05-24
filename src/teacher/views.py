from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.models import Teacher


def generate_teachers(request):
    for _ in range(10):
        Teacher.generate_teacher()
    abc = Teacher.objects.all()
    return HttpResponse(abc)


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers_list'

    def get_queryset(self):
        request = self.request
        qsg = super().get_queryset()

        if request.GET.get('tfname') or request.GET.get('tlname') or request.GET.get('email'):
            qsg = qsg.filter(Q(first_name=request.GET.get('tfname')) | Q(
                last_name=request.GET.get('tlname')) | Q(email=request.GET.get('email')))

        return qsg

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teacher list'
        return context


class TeachersUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherEditForm

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersCreateView(CreateView):
    model = Teacher
    template_name = 'teachers_add.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teachers:list')


class TeachersDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers_delete.html'

    def get_success_url(self):
        return reverse('teachers:list')
