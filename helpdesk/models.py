from msilib.schema import Class
from django.db import models

# Create your models here.
class Topicos(models.Model):
    titulo = models.CharField(max_length=320, blank=False, null=False)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo

class Procedimento(models.Model):
    topicos = models.ForeignKey(Topicos, on_delete=models.PROTECT)
    passo_a_passo = models.TextField(blank=False, null=False)
    sucesso = models.TextField(blank=True, null=True)
    falha = models.TextField(blank=True, null=True)
    relacionados = models.ManyToManyField('Procedimento')
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)


    def __str__(self) -> str:
        return self.passo_a_passo