from django import forms
from django.core.exceptions import ValidationError


class VagaForm(forms.Form):
    titulo = forms.CharField(max_length=150)
    empresa = forms.CharField(max_length=150)
    telefone = forms.CharField(max_length=20)
        
    def clean_titulo(self):
        nome = self.cleaned_data['titulo']
        return nome.upper()

    def clean_empresa(self):
        empresa = self.cleaned_data['empresa']
        if len(empresa) < 3:
            raise ValidationError('Empresa precisa ter ao menos três caracteres')
        return empresa

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone.startswith('19'):
            return telefone
        raise ValidationError('DDD válido somente o 19')
