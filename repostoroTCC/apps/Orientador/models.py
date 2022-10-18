from django.db import models

class Orientador(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    link_curriculo = models.URLField()

    def __str__(self):
        return self.first_name + " " + self.last_name