from django.db import models

class PontoTurstico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    #atracoes = models.ManyToManyField(Atracao)
    #comentarios = models.ManyToManyField(Comentario)
    #avaliacoes = models.ManyToManyField(Avaliacao)
    #endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
