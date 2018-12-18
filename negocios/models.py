from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Acao(models.Model):
    sigla = models.CharField(max_length=25)
    empresa = models.ForeignKey(Empresa, related_name="acoes", on_delete= models.CASCADE)
    data_inicio = models.DateTimeField()

    def __str__(self):
        return self.sigla.__str__() + " / " + self.empresa.__str__()

class Cotacao(models.Model):
    data = models.DateTimeField()
    acao = models.ForeignKey(Acao, related_name="cotacoes", on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=15)

