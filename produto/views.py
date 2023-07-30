from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('ListaProduto')
class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProduto')
class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao Carrinho')
class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do Carrinho')
class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')