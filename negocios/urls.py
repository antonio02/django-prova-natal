from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.empresas, name='empresas'),
    path('empresas/add/', views.empresas_add, name='empresas_add'),
    path('acoes/', views.acoes, name='acoes'),
    path('acoes/add/', views.acoes_add, name='acoes_add'),
    path('cotacoes/', views.cotacoes, name='cotacoes'),
    path('cotacoes/add/', views.cotacoes_add, name='cotacoes_add')
]