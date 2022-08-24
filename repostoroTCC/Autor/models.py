from django.db import models

class Autor(models.Model):
    primeiro_nome = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    ultimo_nome = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    foto = models.ImageField(upload_to="imagens/")

    def __str__(self):
        return self.primeiro_nome + " " + self.ultimo_nome