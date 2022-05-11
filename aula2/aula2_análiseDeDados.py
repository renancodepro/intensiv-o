import pandas as pd
import plotly.express as px

# passo 1: Importar a base de dados
# ler o arquivo csv e armazena na variavel tabela
tabela = pd.read_csv('telecom_users.csv')
# passo 2: Visualizar a base da dados
# Entender as informações dque você tem disponível
# Para você corrigir as cagadas da base de dados

# Exclui coluna/linha
# axis=0 -. linha, axis=1 -> coluna
tabela = tabela.drop('Unnamed: 0', axis=1)
# Passo 3: Tratamento de dados
# ver e ajustar qualquer valor que esteja sendo reconhecido de forma errada

# transformando a coluna totalgasto e transformar em númerico pois está sendo
# reconhecida como object(texto)
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# valores vazios
# colunas vazias -> exclui
tabela = tabela.dropna(how='all', axis=1)
# Linhas com algum valor vazios -> excluir
tabela = tabela.dropna(how='any', axis=0)

# mostra toda informações da tabela
print(tabela.info())

# Passo 4: Análise simples -> entender como estão acontecendo os cancelamentos
# conta os valores
print(tabela['Churn'].value_counts())
# conta os valores e mostra em percentual
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise mais completa -> entender a causa dos cancelamentos e
# cria grafico
# para cada coluna da base de dados gerar um grafico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    # exibe gráfico
    grafico.show()

# possíveis soluções
