from django.test import TestCase
from .models import Paciente
from django.utils import timezone

class PacienteModelTest(TestCase):

    def test_criar_paciente(self):
        paciente = Paciente.objects.create(
            nome="João",
            idade=30,
            sintomas="Febre",
            prioridade="U",
            data_consulta=timezone.now()
        )
        self.assertEqual(paciente.nome, "João")
        self.assertEqual(paciente.prioridade, "U")
