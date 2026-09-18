from django import forms
from .models import Receita, Despesas, Caixinha, Categoria_Despesa, Categoria_Receita, Previsao

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = [ 'valor', 'descricao', 'data', 'categoria']

class DespesasForm(forms.ModelForm):
    class Meta:
        model = Despesas
        fields = ['descricao', 'valor', 'data', 'categoria']

MESES = [
    (1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'),
    (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'),
    (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro'),
]

class PreReceitaForm(forms.Form):
    mes = forms.ChoiceField(choices=MESES, label='Mês')
    ano = forms.IntegerField(min_value=2020, max_value=2100, label='Ano')

class PreDespesasForms(forms.Form):
    mes = forms.ChoiceField(choices=MESES, label='Mês')
    ano = forms.IntegerField(min_value=2020, max_value=2100, label='Ano')

class CaixinhasForm(forms.ModelForm):
    class Meta:
        model = Caixinha
        fields = ['nome', 'valor']

class CategoriaReceitaForms(forms.ModelForm):
    class Meta:
        model = Categoria_Receita
        fields = ['categoria']

class PreAdicaoReceita(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria_Receita.objects.none(), empty_label='Escolha a Categoria')

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset=(Categoria_Receita.objects.filter(usuario=usuario))


class CategoriaDespesaForms(forms.ModelForm):
    class Meta:
        model = Categoria_Despesa
        fields = ['categoria']

class EscolherCategoriaDEspesaForms(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria_Receita.objects.none(), empty_label='Escolha a Categoria')

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset=Categoria_Despesa.objects.filter(usuario=usuario)

class escolherPrevisaoForm(forms.Form):
    mes = forms.ChoiceField(choices=MESES)
    ano = forms.IntegerField(min_value=2020, max_value=2100)

class AdicionarPrevisoesForm(forms.ModelForm):
    class Meta:
        model = Previsao
        fields = ['nome', 'valor', 'data', 'ano']
