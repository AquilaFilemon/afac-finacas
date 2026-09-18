# AFAC Finanças

Sistema de finanças pessoais desenvolvido em Django, para acompanhamento de receitas, despesas, investimentos e planejamento financeiro.

## Funcionalidades

- **Receitas e Despesas**: cadastro e acompanhamento do mês atual
- **Histórico**: consulta de meses anteriores
- **Previsão**: planejamento de receitas e despesas para meses futuros
- **Caixinhas**: reserva de valores para objetivos específicos
- **Categorias**: organização de receitas e despesas por categoria
- **Investimentos**: acompanhamento de carteira (ações, FIIs, renda fixa e cripto), com foco em valores e rentabilidade

## Tecnologias

- Python / Django
- SQLite
- HTML / CSS

## Como rodar o projeto localmente

1. Clone o repositório:
```bash
   git clone https://github.com/seu-usuario/AFAC_Financas.git
   cd AFAC_Financas
```

2. Crie e ative o ambiente virtual:
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/Mac
```

3. Instale as dependências:
```bash
   pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz com:SECRET_KEY=sua_chave_secreta_aqui
(gere uma com `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)

5. Rode as migrações:
```bash
   python manage.py migrate
```

6. Inicie o servidor:
```bash
   python manage.py runserver 0.0.0.0:8000
   Acesse: Endereço_IPV4:8000
```

## Status

Projeto em desenvolvimento.