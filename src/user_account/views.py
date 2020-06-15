from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm, UserProfileUpdateForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForm

    def get_success_url(self):
        messages.success(self.request, "New user has been successfully created!")
        return reverse('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Login as a user'}

    def get_success_url(self):
        messages.success(self.request, "You've just successfully logged in")
        return reverse('user_account:profile')


class UserAccountLogoutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Logout from LMS'}


class UserAccountUpdateView(UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Edit current user profile'}
    form_class = UserAccountProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')


@login_required
def user_account_update_profile(request):
    if request.method == 'POST':
        u_form = UserAccountProfileForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!', extra_tags='alert')
            return redirect('user_account:profile')

    else:
        u_form = UserAccountProfileForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': f'Edit {request.user.get_full_name()} user profile'
    }

    return render(
        request=request,
        template_name='profile.html',
        context=context
    )
