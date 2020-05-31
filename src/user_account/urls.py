from django.urls import path
from user_account.views import CreateUserAccountView

app_name = 'user_account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
]
