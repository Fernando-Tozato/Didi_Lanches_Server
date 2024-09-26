from django.contrib import admin
from .models import *


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'user', 'valor_total']
    search_fields = ['id', 'user__username', 'valor_total']
    list_filter = ['data']


@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ['venda', 'produto', 'quantidade', 'preco']
    search_fields = ['venda__id', 'produto__nome']


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'tipo']
    search_fields = ['nome']
    list_filter = ['tipo']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade', 'unidade']
    search_fields = ['nome']


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'material', 'quantidade']


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ['data', 'tipo', 'material', 'produto', 'quantidade', 'user']
    list_filter = ['data', 'tipo']
    search_fields = ['material__nome', 'produto__nome', 'user__username']
