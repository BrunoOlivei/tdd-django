from django.db import models


class Animal(models.Model):
    nome = models.CharField(max_length=50, default="n/a")
    predador = models.BooleanField(default=False )
    venenoso = models.BooleanField(default=False)
    domestico = models.BooleanField(default=False)

    def __str__(self):
        return self.nome