from django.urls import path
from sensores import views

urlpatterns = [
    path('api/leitura/', views.api_leitura),
]
