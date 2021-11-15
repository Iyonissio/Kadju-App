from django.db import models


class Destaque(models.Model):
    nome = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.nome
