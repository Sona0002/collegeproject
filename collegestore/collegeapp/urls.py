from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('form',views.form,name='form'),
    path('logout',views.logout,name='logout'),
    path('success',views.success,name='success'),



]