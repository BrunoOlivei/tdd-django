from django.db import models


class Animal(models.Model):
    nome = models.CharField(max_length=50)
    predador = models.BooleanField()
    venenoso = models.BooleanField()
    domestico = models.BooleanField()

    def __str__(self):
        return self.nome