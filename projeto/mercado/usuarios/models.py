from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=45)
    perecivel = models.BooleanField(default=False)
    preco = models.FloatField()
    marca = models.CharField(max_length=25)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
    