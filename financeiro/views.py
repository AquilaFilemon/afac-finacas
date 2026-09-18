from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Receita, Despesas, Caixinha, Categoria_Receita, Categoria_Despesa, Previsao
from .forms import ReceitaForm, DespesasForm, PreReceitaForm, PreDespesasForms, CaixinhasForm, CategoriaDespesaForms, CategoriaReceitaForms, PreAdicaoReceita, EscolherCategoriaDEspesaForms, escolherPrevisaoForm, AdicionarPrevisoesForm
from django.utils import timezone
from django.db.models import Sum

# Create your views here.

#----------------------------------------------------------------RECEITAS-----------------------------------------------------------------------------------------
@login_required
def preReceita(request):
    if request.method == 'POST':
        form = PreReceitaForm(request.POST)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            return redirect(f"/financeiro/receitas/?mes={mes}&ano={ano}")
    else:
        hoje = timezone.now()
        form = PreReceitaForm(initial={'mes': hoje.month, 'ano': hoje.year})
    return render(request, 'financeiro/preReceita.html', {'form': form})

@login_required
def receitas(request):
    hoje = timezone.now()
    mes = int(request.GET.get('mes', hoje.month))
    ano = int(request.GET.get('ano', hoje.year))
    receitas = Receita.objects.filter(usuario=request.user, data__month=mes, data__year=ano)
    """
        Aqui eu crio uma varável que irá receber os registros do usuário
        receita.objects é o gerenciador pelo qual que faço pesquisas no banco
        Aplico o filter ao gerenciado e passo o nome do usuário
    """
    return render(request, 'financeiro/receitas.html', {"receitas":receitas})

@login_required
def preAdicionarReceita(request):
    if request.method == 'POST':
        form = PreAdicaoReceita(request.POST, usuario=request.user)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            return redirect(f'/financeiro/adicionar_receitas/?categoria={categoria.id}')
    else:
        form = PreAdicaoReceita(usuario=request.user)
    return render(request, 'financeiro/preAdicaoReceita.html', {'form':form})

@login_required
def categoriaReceitaAdicionar(request):
    if request.method == 'POST':
        form = CategoriaReceitaForms(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.usuario = request.user
            categoria.save()
            return redirect('preReceita')
    else:
        form = CategoriaReceitaForms()
    return render(request, 'financeiro/criarCategoriaReceita.html', {'form': form})

@login_required
def categoriasReceitas(request):
    categorias = Categoria_Receita.objects.filter(usuario = request.user)
    return render(request, 'financeiro/categoriasReceita.html', {'categorias' : categorias})

@login_required
def editarCategoriaReceita(request, id):
    categoria = get_object_or_404(Categoria_Receita, id=id)
    if request.method == 'POST':
        form = CategoriaReceitaForms(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('preReceita')
    else:
        form = CategoriaReceitaForms(instance=categoria)
    return render(request, 'financeiro/editarCategoria.html', {'form':form})

@login_required
def excluirCategoriaReceita(request, id):
    categoria = get_object_or_404(Categoria_Receita, id = id)
    categoria.delete()
    return redirect('preAdicaoReceita')

    
@login_required
def adicionar_receitas(request):
    categoria_id = request.GET.get('categoria')
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        """"Aqui ele vai entrar se eu estiver enviado o formulario"""
        if form.is_valid():
            """Ele vai testar se o formulario é válido"""
            receita = form.save(commit=False)
            """
            Aqui eu configuro o formulário para salvar no banco de dados, mas não salvo ainda por isos o commite=false
            """
            receita.usuario = request.user
            """Aqui eu defino o usuário de receita como o user que está no request"""
            receita.categoria_id = categoria_id
            receita.save()
            return redirect('preReceita')
    else:
        form = ReceitaForm()
    """Aqui vai entrar se o metodo for GET (se ele estiver só puxando o formulário para preencher)"""
    return render(request, 'financeiro/adicionar_receita.html', {'form' : form})

@login_required
def editar_receita(request, id):
    despesas = get_object_or_404(Receita, id = id)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=despesas)
        if form.is_valid():
            form.save()
            return redirect('preReceita')
    else:
        form = ReceitaForm(instance=despesas)
    return render(request, 'financeiro/editar_receita.html', {'form':form})

@login_required
def excluir_receita(request, id):
    receita = get_object_or_404(Receita, id=id)
    receita.delete()
    return redirect('receitas')
#----------------------------------------------------------------RECEITAS-----------------------------------------------------------------------------------------

#----------------------------------------------------------------DESPESAS-----------------------------------------------------------------------------------------

def preDespesa(request):
    if request.method == 'POST':
        form = PreDespesasForms(request.POST)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            return redirect(f'/financeiro/despesas/?mes={mes}&ano={ano}')
            
    else:
        hoje = timezone.now()
        form = PreDespesasForms(initial = {'mes': hoje.month, 'ano': hoje.year})
    return render(request, 'financeiro/preDespesa.html', {'form': form})


@login_required
def despesas(request):
    hoje = timezone.now()
    mes = int(request.GET.get('mes', hoje.month))
    ano = int(request.GET.get('ano', hoje.year))
    despesas = Despesas.objects.filter(usuario = request.user, data__month = mes, data__year = ano)
    return render(request, 'financeiro/despesas.html', {'despesas' : despesas})


@login_required
def adicionar_despesas (request):
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            return redirect('preDespesa')
    else:
        form = DespesasForm()
    return render(request, 'financeiro/adicionar_despesas.html', {'form' : form})

@login_required
def escolherCategoriaDespesa(request):
    if request.method == 'POST':
        form = EscolherCategoriaDEspesaForms(request.POST, usuario=request.user)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            return redirect(f'/financeiro/adicionar_despesas/?categoria={categoria.id}')
    else:
        form = EscolherCategoriaDEspesaForms(usuario=request.user)
        return render(request, 'financeiro/escolherCategoriaDespesa.html', {'form':form})
    
@login_required
def adicionarCategoriaDespesa(request):
    if request.method == 'POST':
        form = CategoriaDespesaForms(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.usuario = request.user
            categoria.save()
            return redirect('escolherCategoriaDespesa')
    else:
        form = CategoriaDespesaForms()
    return render(request, 'financeiro/adicionarCategoriaDespesa.html', {'form': form})

@login_required
def categoriasDespesas(request):
    categorias = Categoria_Despesa.objects.filter(usuario = request.user)
    return render(request, 'financeiro/categoriaDespesa.html', {'categorias': categorias})

@login_required
def excluirCategoriaDespesa(request, id):
    categoria = get_object_or_404(Categoria_Despesa, id=id)
    categoria.delete()
    return redirect('categoriasDepesas')

@login_required
def editarCategoriaDespesa(request, id):
    categoria = get_object_or_404(Categoria_Despesa, id=id)
    if request.method == 'POST':
        form = CategoriaDespesaForms(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('escolherCategoriaDespesa')
    else:
        form = CategoriaDespesaForms(instance=categoria)
    return render(request, 'financeiro/editarCategoriaDespesa.html', {'form':form})

@login_required
def excluir_despesa(request, id):
    despesa = get_object_or_404(Despesas, id=id)
    despesa.delete()
    return redirect('despesas')

def editar_despesa(request, id):
    despesa = get_object_or_404(Despesas, id=id)
    if request.method == 'POST':
        form = DespesasForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('preDespesa')
    else:
        form = DespesasForm(instance=despesa)
        return render(request, 'financeiro/editar_despesa.html', {'form': form})
#----------------------------------------------------------------DESPESAS-----------------------------------------------------------------------------------------

#----------------------------------------------------------------CAIXINHAS-----------------------------------------------------------------------------------------

@login_required
def caixinhas(request):
    caixinhas = Caixinha.objects.filter(usuario = request.user)
    return render(request, 'financeiro/caixinhas.html', {'caixinhas': caixinhas})

@login_required
def criarCaixinhas(request):
    if request.method == 'POST':
        form = CaixinhasForm(request.POST)
        if form.is_valid():
            caixinha = form.save(commit=False)
            caixinha.usuario = request.user
            caixinha.save()
            return redirect('caixinhas')
    else:
        form = CaixinhasForm()
    return render(request,'financeiro/criar_caixinha.html', {'form':form})

@login_required
def excluir_caixinhas(request, id):
    caixinha = get_object_or_404(Caixinha, id=id)
    caixinha.delete()
    return redirect('caixinhas')

@login_required
def editar_caixinhas(request, id):
    caixinha = get_object_or_404(Caixinha, id=id)
    if request.method == 'POST':
        form = CaixinhasForm(request.POST, instance=caixinha)
        if form.is_valid():
            form.save()
            return redirect('caixinhas')
    else:
        form = CaixinhasForm(instance=caixinha)
    return render(request, 'financeiro/editar_caixinhas.html', {'form':form})
#----------------------------------------------------------------PREVISÕES-----------------------------------------------------------------------------------------

@login_required
def escolherPrevisao(request):
    if request.method == 'POST':
        form = escolherPrevisaoForm(request.POST)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            return redirect(f'/financeiro/previsoes/?mes={mes}&ano={ano}')
    else:
        hoje = timezone.now()
        form = escolherPrevisaoForm(initial={'mes': hoje.month, 'ano': hoje.year})
    return render(request, 'financeiro/escolherPrevisao.html', {'form':form})

@login_required
def previsoes(request):
    hoje = timezone.now()
    mes = int(request.GET.get('mes', hoje.month))
    ano = int(request.GET.get('ano', hoje.year))
    previsoes = Previsao.objects.filter(usuario = request.user, data=mes, ano=ano)
    receitas = previsoes.filter(categoria='R')
    despesas = previsoes.filter(categoria='D')
    soma_receita = receitas.aggregate(total=Sum('valor'))['total'] or 0
    soma_despesa = despesas.aggregate(total=Sum('valor'))['total'] or 0
    resultado = soma_receita - soma_despesa

    return render(request, 'financeiro/previsoes.html', {
        'receitas': receitas,
        'despesas': despesas,
        'soma_receita': soma_receita,
        'soma_despesa': soma_despesa,
        'resultado': resultado})


@login_required
def adicionarPrevisaoReceita(request):
    if request.method == 'POST':
        form = AdicionarPrevisoesForm(request.POST)
        if form.is_valid():
            previsao = form.save(commit=False)
            previsao.usuario = request.user
            previsao.categoria = 'R'
            previsao.save()
            return redirect('previsoes')
    else:
        hoje = timezone.now()
        form = AdicionarPrevisoesForm(initial={'ano': hoje.year, 'data': hoje.month})
    return render(request, 'financeiro/adicionarPrevisao.html', {'form': form})

@login_required
def adicionarPrevisaoDespesa(request):
    if request.method == 'POST':
        form = AdicionarPrevisoesForm(request.POST)
        if form.is_valid():
            previsao = form.save(commit=False)
            previsao.usuario = request.user
            previsao.categoria = 'D'
            previsao.save()
            return redirect('previsoes')
    else:
        hoje = timezone.now()
        form = AdicionarPrevisoesForm(initial={'ano': hoje.year, 'data': hoje.month})
    return render(request, 'financeiro/adicionarPrevisao.html', {'form': form})

@login_required
def excluirPrevisao(request, id):
    previsao = get_object_or_404(Previsao, id=id)
    previsao.delete()
    return redirect('previsoes')

@login_required
def editarPrevisao(request, id):
    previsao = get_object_or_404(Previsao, id=id)
    if request.method == 'POST':
        form = AdicionarPrevisoesForm(request.POST, instance=previsao)
        if form.is_valid():
            form.save()
            return redirect('previsoes')
    else:
        form = AdicionarPrevisoesForm(instance=previsao)
    return render(request, 'financeiro/editarPrevisao.html', {'form':form})