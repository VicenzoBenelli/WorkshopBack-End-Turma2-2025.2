from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AddressViewSet

router = DefaultRouter()
router.register(r"addresses", AddressViewSet, basename="address")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),   # Rotas da app core (home e teste)
    path("", include(router.urls)),   # Rotas da API REST
]
