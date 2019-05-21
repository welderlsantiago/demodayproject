from django.db import models

# Create your models here.

class Banda(models.Model):
    IND_CHOICES = [
        ["SIM", "Sim"],
        ["NAO", "Não"]
    ]

    nome = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    genero = models.CharField(max_length=20, null=False)
    independente = models.CharField(max_length=3, null=False, choices = IND_CHOICES)

    def __str__(self):
        return self.nome