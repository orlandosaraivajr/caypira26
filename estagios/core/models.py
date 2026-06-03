from django.db import models

class VagaModel(models.Model):
    titulo = models.CharField('Título da Vaga', max_length=150)
    empresa = models.CharField('Empresa', max_length=150)
    telefone = models.CharField('Telefone', max_length=20)

    def __str__(self):
        return self.titulo
