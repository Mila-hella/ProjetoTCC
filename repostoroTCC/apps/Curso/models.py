from django.db import models

class Curso(models.Model):

    CHOICES_MODALIDADE = [
        ('B', 'Bacharelado'),
        ('L', 'Licenciatura'),
        ('T', 'Tecnologo'),
    ]
    
    nome = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    modalidade = models.CharField(
        max_length=1,
        choices=CHOICES_MODALIDADE,
        null=False
    )

    def __str__(self):
        return self.nome
