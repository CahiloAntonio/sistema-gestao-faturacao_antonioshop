from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Fornecedor
from django.contrib import messages

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/lista_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        codigo = request.POST['codigo']
        preco = request.POST['preco']
        estoque = request.POST['estoque']
        fornecedor_id = request.POST['fornecedor']
        fornecedor = Fornecedor.objects.get(id=fornecedor_id) if fornecedor_id else None
        
        Produto.objects.create(
            nome=nome,
            codigo=codigo,
            preco=preco,
            estoque=estoque,
            fornecedor=fornecedor
        )
        messages.success(request, 'Produto criado com sucesso!')
        return redirect('lista_produtos')
    
    fornecedores = Fornecedor.objects.all()
    return render(request, 'produto/criar_produto.html', {'fornecedores': fornecedores})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.codigo = request.POST['codigo']
        produto.preco = request.POST['preco']
        produto.estoque = request.POST['estoque']
        fornecedor_id = request.POST['fornecedor']
        produto.fornecedor = Fornecedor.objects.get(id=fornecedor_id) if fornecedor_id else None
        produto.save()
        messages.success(request, 'Produto atualizado com sucesso!')
        return redirect('lista_produtos')
    
    fornecedores = Fornecedor.objects.all()
    return render(request, 'produto/editar_produto.html', {'produto': produto, 'fornecedores': fornecedores})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')
    return render(request, 'produto/excluir_produto.html', {'produto': produto})