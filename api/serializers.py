from rest_framework import serializers
from .models import *


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'data', 'user', 'valor_total']


class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = ['id', 'venda', 'produto', 'quantidade', 'preco']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'estoque', 'tipo']


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'nome']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'nome', 'quantidade', 'unidade']


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'produto', 'material', 'quantidade']


class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ['id', 'data', 'tipo', 'material', 'produto', 'quantidade', 'descricao', 'user']
