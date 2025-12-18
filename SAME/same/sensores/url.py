from django.contrib import admin
from django.urls import path
from sensores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('api/leitura/', views.api_leitura, name='api_leitura'),
]
