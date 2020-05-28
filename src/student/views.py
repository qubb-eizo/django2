from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student


def generate_students(request):
    for _ in range(15):
        Student.generate_student()
    abc = Student.objects.all()
    return HttpResponse(abc)


class StudentsListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')

        if request.GET.get('fname') or request.GET.get('lname') or request.GET.get('email'):
            qs = qs.filter(Q(first_name=request.GET.get('fname')) | Q(
                last_name=request.GET.get('lname')) | Q(email=request.GET.get('email')))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Student list'
        return context


class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm

    def get_success_url(self):
        return reverse('students:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit students'
        return context


class StudentsCreateView(CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'students_delete.html'

    def get_success_url(self):
        return reverse('students:list')
