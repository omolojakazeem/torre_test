from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import forms
from . import serializers
from . import models


class Authentication(View):
    template = 'authentication/auth.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('auth:dashboard', request.user.pk)

        register_form = forms.UserRegistrationForm()
        login_form = forms.UserLoginForm()

        context = {
            'register_form': register_form,
            'login_form': login_form,
        }
        return render(request, template_name=self.template, context=context)

    def post(self, request):
        register_form = forms.UserRegistrationForm(request.POST)
        login_form = forms.UserLoginForm(request.POST)
        if 'register' in request.POST:
            print("register")
            if register_form.is_valid():
                email = register_form.cleaned_data['email']
                password = register_form.cleaned_data['password1']

                user = register_form.save(commit=False)
                user.save()
                my_user = authenticate(request, email=email, password=password)
                login(request, my_user)
                messages.add_message(request, messages.SUCCESS, "Login Successful")
                return redirect('auth:dashboard', request.user.pk, )

            else:
                if register_form.errors:
                    for field in register_form:
                        for error in field.errors:
                            messages.add_message(request, messages.INFO, error)
                return redirect('auth:auth_user')

        elif 'login' in request.POST:
            print("login")
            login_form = forms.UserLoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                my_user = authenticate(request, email=email, password=password)

                if my_user is not None:
                    login(request, my_user)
                    return redirect('auth:dashboard', request.user.pk)
                else:
                    messages.add_message(
                        request, messages.INFO,
                        'Invalid Username / Password')
                    return redirect('auth:auth_user')
            else:
                if login_form.errors:
                    for field in login_form:
                        for error in field.errors:
                            messages.add_message(request, messages.INFO, error)
                return redirect('auth:auth_user')


class Dashboard(View):
    template = 'index.html'

    def get(self, request, pk):
        context = {

        }
        return render(request, template_name=self.template, context=context)


class DashboardUserApi(APIView):
    def get(self, request, pk):
        user = models.UserModel.objects.get(pk=pk)
        serialized_user = serializers.UserSerializer(user)
        return Response(serialized_user.data, status.HTTP_200_OK)


class AllUserApi(APIView):
    def get(self, request):
        users = models.UserModel.objects.all()
        serialized_users = serializers.AllUserSerializer(users, many=True)
        return Response(serialized_users.data, status.HTTP_200_OK)
