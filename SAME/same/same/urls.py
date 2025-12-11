from django.contrib import admin
from django.urls import path
from sensores import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.list_leituras, name='list_leituras'),
    path('create/', views.create_leitura, name='create_leitura'),
    path('edit/<int:id>/', views.edit_leitura, name='edit_leitura'),
    path('delete/<int:id>/', views.delete_leitura, name='delete_leitura'),
]

