from django.contrib import admin
from core.models import Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'qtde_disponivel', 'unidade_medida', 'valor_venda', 'data_cadastro')
    list_filter = ('nome', 'usuario',)

admin.site.register(Produto, ProdutoAdmin)

