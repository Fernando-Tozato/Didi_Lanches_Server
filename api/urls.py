from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'vendas', VendaViewSet)
router.register(r'itensvenda', ItemVendaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'tipos', TipoViewSet)
router.register(r'materiais', MaterialViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'movimentacoes', MovimentacaoViewSet)
