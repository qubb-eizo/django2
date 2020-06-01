from django.urls import path
from user_account.views import CreateUserAccountView, UserAccountLoginView, \
    UserAccountLogoutView, UserAccountProfileView

app_name = 'user_account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('profile/', UserAccountProfileView.as_view(), name='profile'),
]
