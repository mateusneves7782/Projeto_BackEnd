from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
