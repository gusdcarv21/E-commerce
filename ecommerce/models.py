from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField()
    idade = models.IntegerField()
    telefone = models.CharField(max_length=14)
    foto = models.ImageField()
    senha = models.CharField(max_length=15)


