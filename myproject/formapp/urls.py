from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name= 'add'),
    path('index/', views.index, name= 'index'),
    path('adres/', views.adres, name= 'adres'),
    path('delete/<int:id>', views.delete, name= 'delete'),
    path('update/<int:id>', views.update, name= 'update'),
    path('upres/<int:id>', views.upres, name= 'upres'),

]