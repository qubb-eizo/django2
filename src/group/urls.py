from django.urls import path
from group.views import generate_group, \
    GroupsListView, GroupsUpdateView, GroupsCreateView, GroupsDeleteView

app_name = 'groups'

urlpatterns = [
    path('', GroupsListView.as_view(), name='list'),
    path('gen/', generate_group, name='gen'),
    path('add/', GroupsCreateView.as_view(), name='add'),
    path('delete/<int:pk>', GroupsDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>', GroupsUpdateView.as_view(), name='edit')
]
