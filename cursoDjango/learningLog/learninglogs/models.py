from django.db import models

class Pessoa(models.Model):
    """A topic the user is learning about."""
    nome = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Descricao(models.Model):
    """Something specific learned about a topic."""
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'descricoes'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."  # Return first 50 characters