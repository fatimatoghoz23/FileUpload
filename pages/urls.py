from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('login/', views.pagelogin, name='login'),
     path('register/', views.register, name='register'),
     path('delete/<int:pk>', views.delete, name='delete'),


    ]