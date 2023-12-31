from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet, AcessorioViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"Categorias", CategoriaViewSet)
router.register(r"Cores", CorViewSet)
router.register(r"Acessorios", AcessorioViewSet)
router.register(r"Veiculos", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]