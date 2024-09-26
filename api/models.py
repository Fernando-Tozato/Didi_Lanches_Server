from django.contrib.auth.models import User
from django.db import models


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_total = models.FloatField()

    def __str__(self):
        return f"Venda {self.id} - {self.valor_total}"


class ItemVenda(models.Model):
    venda = models.ForeignKey('Venda', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return f"Item {self.produto.nome} - Quantidade: {self.quantidade}"


class Tipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Material(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.FloatField()
    unidade = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    quantidade = models.FloatField()

    def __str__(self):
        return f"{self.produto.nome} - {self.material.nome}"


class Movimentacao(models.Model):
    ENTRADA = True
    SAIDA = False
    TIPO_MOVIMENTACAO = [
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    ]

    data = models.DateTimeField(auto_now_add=True)
    tipo = models.BooleanField(choices=TIPO_MOVIMENTACAO)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.FloatField()
    descricao = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.quantidade}"
