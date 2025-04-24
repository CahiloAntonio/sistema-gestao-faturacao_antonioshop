from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Fornecedor, Cliente
from django.contrib import messages
from phonenumber_field.phonenumber import PhoneNumber
from django.core.exceptions import ValidationError

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/lista_produtos.html', {'produtos': produtos})

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/lista_fornecedores.html', {'fornecedores': fornecedores} )

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
def criar_fornecedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        contacto = request.POST['contacto']
        
        try:
            # Converter string para PhoneNumber e validar
            phone_number = PhoneNumber.from_string(contacto, region='AO')  # AO = Angola
            
            if not phone_number.is_valid():
                raise ValidationError("Número de telefone inválido")
            
            Fornecedor.objects.create(
                nome=nome,
                contacto=phone_number
            )
            messages.success(request, 'Fornecedor criado com sucesso!')
            return redirect('lista_fornecedores')
            
        except (ValidationError, ValueError) as e:
            messages.error(request, f'Erro no contacto: {e}')
            return redirect('criar_fornecedor')
    
    return render(request, 'fornecedor/criar_fornecedor.html')
    



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
def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    
    if request.method == 'POST':
        fornecedor.nome = request.POST['nome']
        
        try:
            contacto = request.POST['contacto']
            phone_number = PhoneNumber.from_string(contacto, region='AO')
            
            if not phone_number.is_valid():
                raise ValidationError("Número de telefone inválido")
                
            fornecedor.contacto = phone_number
            fornecedor.save()
            messages.success(request, 'Fornecedor atualizado com sucesso!')
            return redirect('lista_fornecedores')
            
        except (ValidationError, ValueError) as e:
            messages.error(request, f'Erro no contacto: {e}')
            return redirect('editar_fornecedor', pk=pk)
    
    # Formata o número para exibição no formulário
    contexto = {
        'fornecedor': fornecedor,
        'contacto_formatado': str(fornecedor.contacto) if fornecedor.contacto else ''
    }
    return render(request, 'fornecedor/editar_fornecedor.html', contexto)
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')
    return render(request, 'produto/excluir_produto.html', {'produto': produto})

def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        messages.success(request, 'Fornecedor excluído com sucesso!')
        return redirect('lista_fornecedores')
    return render(request, 'fornecedor/excluir_fornecedor.html', {'fornecedor': fornecedor})

