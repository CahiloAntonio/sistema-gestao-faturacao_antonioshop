from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]