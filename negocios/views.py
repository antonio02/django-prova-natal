from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def empresas(request):
    return render(request, 'empresas.html', {'empresas': Empresa.objects.all()})


def acoes(request):
    return render(request, 'acoes.html', {'acoes': Acao.objects.all()})

def cotacoes(request):
    return render(request, 'cotacoes.html', {'acoes': Acao.objects.all()})


def empresas_add(request):
    if request.method == 'POST':
        empresa_form = EmpresaForm(request.POST)

        if empresa_form.is_valid():
            empresa_form.save()
            return redirect(empresas)

        else:
            return render(request, 'empresa_add.html', {'form': EmpresaForm()})

    else:
        return render(request, 'empresa_add.html', {'form': EmpresaForm()})


def acoes_add(request):
    if request.method == 'POST':
        acao_form = AcaoForm(request.POST)

        if acao_form.is_valid():
            acao_form.save()
            return redirect(acoes)

        else:
            return render(request, 'acao_add.html', {'form': AcaoForm()})

    else:
        return render(request, 'acao_add.html', {'form': AcaoForm()})


def cotacoes_add(request):
    if request.method == 'POST':
        cotacao_form = CotacaoForm(request.POST)

        if cotacao_form.is_valid():
            cotacao_form.save()
            return redirect(cotacoes)

        else:
            return render(request, 'cotacao_add.html', {'form': CotacaoForm()})

    else:
        return render(request, 'cotacao_add.html', {'form': CotacaoForm()})