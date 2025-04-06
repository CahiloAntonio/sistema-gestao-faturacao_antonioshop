from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('lista_produtos'), name='home'),  # Redireciona / para /produtos/
    path('', include('vendas.urls')),
]