from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True, null=True)
    unidade_medida = models.CharField(max_length=4)
    qtde_estoque = models.DecimalField(max_digits=10, decimal_places=4)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=4)
    qtde_reservada = models.DecimalField(max_digits=10, decimal_places=4)
    qtde_disponivel = models.DecimalField(max_digits=10, decimal_places=4)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=4)
    data_cadastro = models.DateTimeField(auto_now=True, verbose_name='Data de Cadastro')
    data_desativacao = models.DateTimeField(auto_now=True)
    status = models.BooleanField(null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=30, null=True)
    tamanho = models.CharField(max_length=3)
    cor = models.CharField(max_length=20)
    cod_origem = models.IntegerField(null=True)
    cod_gtin_ean = models.IntegerField(null=True)



    class Meta:
        db_table = 'Produto'

    def __str__(self):
        return self.nome

    def get_data_cadastro(self):
        return self.data_cadastro.strftime('%d/%m/%Y %H:%M')

