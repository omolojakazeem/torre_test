from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('auth/', views.Authentication.as_view(), name='auth_user'),
    path('dashboard/<int:pk>', views.Dashboard.as_view(), name='dashboard'),
    path('mydetail/<int:pk>', views.DashboardUserApi.as_view(), name='user_list_api'),
    path('all/', views.AllUserApi.as_view(), name='user_list'),
]
