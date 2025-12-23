from django.urls import path
from . import views

app_name = 'learninglogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('pessoas/', views.pessoas, name='pessoas'),  # Rota para a página de pessoas
    path('pessoa/<pessoa_id>/', views.pessoa, name='pessoa'), # Rota para a página de pessoa individual
]
