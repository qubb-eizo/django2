from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


def generate_students(request):
    for _ in range(15):
        Student.generate_student()
    abc = Student.objects.all()
    return HttpResponse(abc)


class StudentsListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'
    login_url = reverse_lazy('user_account:login')
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('group')

        if self.request.GET.get('fname') or self.request.GET.get('lname') or self.request.GET.get('email'):
            qs = qs.filter(Q(first_name=self.request.GET.get('fname')) | Q(
                last_name=self.request.GET.get('lname')) | Q(email=self.request.GET.get('email')))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        params = self.request.GET

        context['title'] = 'Student list'
        context['query_params'] = urlencode({k: v for k, v in params.items() if k != 'page'})
        return context


class StudentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('students:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit students'
        return context


class StudentsCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students_delete.html'
    login_url = reverse_lazy('user_account:login')

    def get_success_url(self):
        messages.success(self.request, f'Student has been deleted!')
        return reverse('students:list')
