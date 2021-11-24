from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = models.UserModel
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        super(UserRegistrationForm, self).clean()
        email = self.cleaned_data.get('email')

        if email is None:
            self._errors['email'] = self.error_class([
                'Please provide your email address'])

        return email.lower()

    def clean(self):
        super(UserRegistrationForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 is None:
            self._errors['password1'] = self.error_class([
                'Please provide your password'])

        if password1 == password2:
            pass
        else:
            self._errors['password2'] = self.error_class([
                'Your passwords must me the same'])

        return self.cleaned_data


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    fields = ['email', 'password']

    def clean_email(self):
        super(UserLoginForm, self).clean()
        email = self.cleaned_data.get('email')

        if email is None:
            self._errors['email'] = self.error_class([
                'Email is required'])

        return email.lower()

    def clean(self):
        super(UserLoginForm, self).clean()
        password = self.cleaned_data.get('password')

        if password is None:
            self._errors['password'] = self.error_class([
                'Please enter your password'])

        return self.cleaned_data
