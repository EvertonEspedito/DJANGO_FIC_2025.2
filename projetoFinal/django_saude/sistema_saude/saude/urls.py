from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_pacientes, name='listar_pacientes'),
    path('novo/', cadastrar_paciente, name='cadastrar_paciente'),
    path('editar/<int:id>/', editar_paciente, name='editar_paciente'),
    path('excluir/<int:id>/', excluir_paciente, name='excluir_paciente'),
    path('dashboard/', dashboard, name='dashboard'),
    path('confirmar/<int:id>/', confirmar_atendimento, name='confirmar_atendimento'),
    path('relatorio/', relatorio_atendidos, name='relatorio_atendidos'),
]
