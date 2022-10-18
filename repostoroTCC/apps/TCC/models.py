from django.db import models
# from Orientador.models import Orientador
# from Autor.models import Autor
# from Curso.models import Curso
from django.contrib.postgres.fields import ArrayField


class TCC(models.Model):

    titulo = models.CharField(
        max_length = 100,
        blank = False,
        null = False,
    )
    autor = models.ForeignKey(
        "Autor.Autor",
        on_delete=models.CASCADE
    )
    orientador = models.ForeignKey(
        "Orientador.Orientador",
        on_delete=models.CASCADE
    )
    curso = models.ForeignKey(
        "Curso.Curso",
        on_delete=models.CASCADE,
    )
    ano_documento = models.IntegerField(
        verbose_name = "Ano da Publicação do Documento",
    )
    resumo = models.TextField()
    arquivo_documento = models.FileField(
        upload_to='arquivos/',
    )

    palavras_chave = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self) -> str:
        return self.titulo