from django.db import models
from django.contrib.auth.models import User

class Categoria_Receita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Categoria_Despesa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Receita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    """
        usuario: é o nome campo do banco de dados
        
        models.ForeignKey: Crio um relacioanmento de muitos para 1 entre duas tabelas. 
        pois um usuário pode ter várias receitas. Na prática, o sistema cria duas tabelas,
        uma para usuário e uma para as receitas. Na tabela de receitas ele vai ligar pelo id a de usuário

        User: É o model User

        on_delete=models.CASCADE: Eu digo que quando o usuário for apagado, 
        o django deve apagar todas as receitas viculada aquele usuário
    """
    descricao = models.CharField(max_length=100)
    """
        models.CharField: é o campo para armazenar textos curtos
    """
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria_Receita, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return super().__str__()
    """
        Essa função eu uso para representar de modo legível o que está escrito no model
        Sem ela, quando eu desse um: print(receita) apareceria: Receita object (1)
        Com a função __str__, quando eu der um print(receita) -> internamento o sistema fará: receita.__str__()
        e retornará: "salario"
        É recomendável que todo Model do Django tenha um método __str__, retornando a informação que melhor identifica aquele registro.
        Por exemplo:
        Usuário: return self.username
        Receita: return self.descricao
        Despesa: return self.descricao
        Categoria: return self.nome
    """

class Despesas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria_Despesa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descricao

class Caixinha(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=25)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Previsao(models.Model):
    OPCOES = [
        ('D', 'Despesas'),
        ('R', 'Receitas')
    ]
    MESES = [
    (1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'),
    (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'),
    (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.IntegerField(choices=MESES)
    ano = models.IntegerField()
    categoria = models.CharField(max_length=1, choices=OPCOES)

    def __str__(self):
        return self.nome