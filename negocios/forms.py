from django import forms
from .models import *

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome']

class AcaoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ['sigla', 'empresa', 'data_inicio']

class CotacaoForm(forms.ModelForm):
    class Meta:
        model = Cotacao
        fields = ['data', 'acao', 'valor']