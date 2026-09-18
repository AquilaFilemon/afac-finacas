from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import formularioLogin, CadastroForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.utils import timezone
from financeiro.models import Receita, Despesas



class CustonLoginView(LoginView):
    authentication_form = formularioLogin

@login_required
def home(request):
    hoje = timezone.now()
    mes_atual = hoje.month
    ano_atual = hoje.year

    total_receita = Receita.objects.filter(usuario=request.user).aggregate(total=Sum('valor'))['total'] or 0
    total_despesa = Despesas.objects.filter(usuario=request.user).aggregate(total=Sum('valor'))['total'] or 0
    """ Aqui eu estou colocando na variável os valores das receitas
        Primeiro eu aplico um filter onde eu pego todas as entradas do usuário em receita
        Depois eu aplico o aaggregate para somar todas essas entradas
        Depois eu pego só o 'total gerado pelo aaddregate', vito que ele gera um dicionario
        E coloco um if reuzido que diz que se não tiver entradas ele vai retornar 0
    """
    saldo_atual = total_receita - total_despesa

    receita_mes = Receita.objects.filter(
        usuario=request.user,
        data__year=ano_atual,
        data__month=mes_atual
        ).aggregate(total=Sum('valor'))['total'] or 0

    despesas_mes = Despesas.objects.filter(
        usuario=request.user,
        data__year=ano_atual,
        data__month=mes_atual
        ).aggregate(total=Sum('valor'))['total'] or 0

    context = {
        'saldo_atual': saldo_atual,
        'receita_mes': receita_mes,
        'despesa_mes': despesas_mes,
    }
    """Aqui é um dicionário que eu passo para o home.html todos os calculos que fiz"""


    return render(request, 'home.html', context)

def cadastro(request):
    if request.method == 'POST':
        #Aqui eu testo se a pessoa está enviado o formulario (metodo POST)
        form = CadastroForm(request.POST)
        #Crio um obejto do tipo UserCreationForm
        if form.is_valid():
        #Vejo se os dados são válidos
            form.save()
            #Salvo os dados no banco de dados
            return redirect('login')
    else:
        form = CadastroForm()
        #Aqui ele vai entrar se o metodo for GET(entradando no formuario), ai ele vai abrir o formulario

    return render(request, 'cadastro.html', {'form' : form}) 
    #Aqui a view vai retornar o render do cadastro.html passando a instância form, que vai ter o formula´rio cirado pelo UserCreationForm
