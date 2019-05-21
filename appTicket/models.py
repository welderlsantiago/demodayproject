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


class GrupoBandas(models.Model):
    estado_opcoes = [
        ["Acre", 'Acre'],
        ["Amapá", 'Amapá'],
        ["Amazonas",'Amazonas'],
    ]

    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    estado = models.CharField(max_length=15, choices= estado_opcoes)
    biografia = models.CharField(max_length=300)
    foto = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.nome