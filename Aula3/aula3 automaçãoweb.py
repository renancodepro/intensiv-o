from selenium import webdriver  # criar o navegador
from selenium.webdriver.common.by import By  # localizar elementos
from selenium.webdriver.common.keys import Keys  # permitar clickar teclas
import pandas as pd

# chromedriver -> chrome
# geckodriver -> firefox
navegador = webdriver.Chrome()

# Passo 1: entrar no google
navegador.get('https://www.google.com/')

# Passo 2: pesquisar a cotação do dólar
# encontrar elemento
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# Passo 3: pegar a cotação do dólar
cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Passo 4: pegar a cotação do euro
navegador.get('https://www.google.com/')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação do euro')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


# Passo 5: Pegar a cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')


# Passo 6: Atualizar a minha base de dados com as novas cotações
# lendo minha tabela
tabela = pd.read_excel('Produtos.xlsx')

# atualizar a cotação de acordo com a moeda correspondente
# dolar
# as linhas onde a coluna '
# Moeda' == 'Dólar'
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
# euro
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
# ouro
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)
# atualizar preço de compra = preço original * cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# atualizar preço de vendas = preço de compra * margem
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

print(tabela)

# Exportar a nova base de preços atualizada
tabela.to_excel('ProdutosAtualizados.xlsx', index=False)
navegador.quit()
