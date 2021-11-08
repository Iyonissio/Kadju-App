from django.db import models

class Destaque(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
