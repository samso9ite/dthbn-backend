from django.urls import path, re_path

# from django.conf.urls import url, include
from django.urls import re_path as url
from . import views
from django.contrib.auth.urls import views as auth_views

app_name = 'Auth'

urlpatterns = [
    path('sign_up', views.sign_up_view, name='Register'),
    path('login', views.login_view, name='Login'),
    path('activate',views.activate, name='activate'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('reset-password/<str:uidb64>/<str:token>', views.reset_password, name='reset-password'),
    path('logout/', views.logout_view, name="logout"),
    path('resetPassword/', views.change_password_view, name="sch_pwd_reset"),
    path('adminPasswordReset/', views.change_password_view, name="adminPasswordReset"),  
]