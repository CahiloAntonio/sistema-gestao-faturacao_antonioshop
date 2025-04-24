from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.add()

# Modelo Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contacto = PhoneNumberField(region='AO', blank=True, null=True)  # Define Angola como padrão
    
    def __str__(self):
        return self.nome

# Modelo Produto
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

# Modelo Venda
class Venda(models.Model):
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Venda {self.id} - {self.data}"

# Modelo Itens_Venda (relacionamento muitos-para-muitos com chave composta)
class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('venda', 'produto')  # Chave primária composta

    def __str__(self):
        return f"{self.produto.nome} ({self.quantidade}) - Venda {self.venda.id}"
