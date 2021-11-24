from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('auth/', views.Authentication.as_view(), name='auth_user')
]