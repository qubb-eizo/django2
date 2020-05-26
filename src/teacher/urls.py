from django.urls import path
from teacher.views import generate_teachers, \
    TeachersListView, TeachersCreateView, TeachersDeleteView, TeachersUpdateView

app_name = 'teachers'

urlpatterns = [
    path('', TeachersListView.as_view(), name='list'),
    path('gen/', generate_teachers, name='gen'),
    path('add/', TeachersCreateView.as_view(), name='add'),
    path('edit/<int:pk>', TeachersUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', TeachersDeleteView.as_view(), name='delete')
]
