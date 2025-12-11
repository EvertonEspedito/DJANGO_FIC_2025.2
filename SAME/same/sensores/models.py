from django.db import models

class Leitura(models.Model):
    temperatura = models.FloatField()
    umidade = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperatura}°C - {self.umidade}%"
