from django.db import models

class Paciente(models.Model):

    PRIORIDADE_CHOICES = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
        ('U', 'Urgente'),
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sintomas = models.TextField()
    prioridade = models.CharField(
        max_length=1,
        choices=PRIORIDADE_CHOICES,
        default='M'
    )
    data_consulta = models.DateTimeField()
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
