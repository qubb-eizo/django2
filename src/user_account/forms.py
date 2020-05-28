from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserAccountRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):

        email = self.cleaned_data['email']

        if User.objects.all().filter(email=email).exists():
            raise ValidationError('Email already exists')

        return email

    def clean(self):

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if first_name == last_name:
            raise ValidationError('First and Last name already exists')

        return self.cleaned_data
