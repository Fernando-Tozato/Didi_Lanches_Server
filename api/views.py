from rest_framework import viewsets
from .serializers import *


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
