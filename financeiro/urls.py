from django.urls import path
from . import views

urlpatterns = [
#-------------------------------------------------------RECEITAS----------------------------------------------------------#
    path('preReceita/', views.preReceita, name='preReceita'),
    path('receitas/', views.receitas, name='receitas'),
    path('preAdicaoReceita', views.preAdicionarReceita, name='preAdicaoReceita'),
    path('categoriasReceita', views.categoriasReceitas, name='categoriasReceita'),
    path('editarCategoriaReceita/<int:id>/', views.editarCategoriaReceita, name='editarCategoriaReceita'),
    path('excluirCategoriaReceita/<int:id>/', views.excluirCategoriaReceita, name='excluirCategoriaReceita'),
    path('adicionar_receitas/', views.adicionar_receitas, name='adicionar_receitas'),
    path('receita/editar/<int:id>/', views.editar_receita, name='editar_receita'),
    path('receitas/exluir/<int:id>/', views.excluir_receita, name='excluir_receita'),
    path('criarCategoriaReceitaAdicionar/', views.categoriaReceitaAdicionar, name='criarCategoriaReceitaAdicionar'),
#-------------------------------------------------------RECEITAS----------------------------------------------------------#

#-------------------------------------------------------DESPESAS----------------------------------------------------------#
    path('preDespesa/', views.preDespesa, name='preDespesa'),
    path('despesas/', views.despesas, name='despesas'),
    path('escolherCategoriaDespesa', views.escolherCategoriaDespesa, name='escolherCategoriaDespesa'),
    path('adicionarCategoriaDespesa/', views.adicionarCategoriaDespesa, name='adicionarCategoriaDespesa'),
    path('categoriasDespesas', views.categoriasDespesas, name='categoriasDepesas'),
    path('excluirCategoriaDespesas/<int:id>', views.excluirCategoriaDespesa, name='excluirCategoriaDespesas'),
    path('editarCategoriaDespesa/<int:id>', views.editarCategoriaDespesa, name='editarCategoriaDespesa'),
    path('adicionar_despesas/', views.adicionar_despesas, name='adicionar_despesas'),
    path('despesas/excluir/<int:id>/', views.excluir_despesa, name='excluir_despesas'),
    path('depesas/editar/<int:id>/', views.editar_despesa, name='editar_despesa'),
#-------------------------------------------------------DESPESAS----------------------------------------------------------#

#-------------------------------------------------------CAIXINHAS----------------------------------------------------------#
    path('caixinhas/', views.caixinhas, name='caixinhas'),
    path('criarCaixinhas/', views.criarCaixinhas, name='criarCaixinhas'),
    path('caixinhas/editar/<int:id>/', views.editar_caixinhas, name='editar_caixinha'),
    path('caixinhas/excluir/<int:id>/', views.excluir_caixinhas, name='excluir_caixinha'),
#-------------------------------------------------------CAIXINHAS----------------------------------------------------------#
#-------------------------------------------------------PREVISAO----------------------------------------------------------#
    path('escolherPrevisao/', views.escolherPrevisao, name='escolherPrevisao'),
    path('previsoes/', views.previsoes, name='previsoes'),
    path('adicionarPrevisaoReceita/', views.adicionarPrevisaoReceita, name='adiconarPrevisaoReceita' ),
    path('adiconarPrevisaoDespesa/', views.adicionarPrevisaoDespesa, name='adicionarPrevisaoDespesa'),
    path('excluirPrevisao/<int:id>/', views.excluirPrevisao, name='excluirPrevisao'),
    path('editarPrevisao/<int:id>/', views.editarPrevisao, name='editarPrevisao'),
]