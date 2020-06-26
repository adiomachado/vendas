from django.shortcuts import render
from core.models import Produto

# Create your views here.
"""
Uma maneira de redirecionar a view quando informar so a rota http://127.0.0.1:8000/
vai redirecionar para o diretorio /vendas , sera preciso fazer o import do redirect
def index(request):
    return redirect('/vendas/')
"""

def lista_produtos(request):
    #usuario = request.user
    #produto = Produto.objects.filter(usuario=usuario)
    produto = Produto.objects.all()
    dados = {'produtos': produto}
    return render(request, 'produto.html', dados)