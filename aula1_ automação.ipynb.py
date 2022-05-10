import pyautogui
import pyperclip
import time
import pandas as pd

# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla

pyautogui.PAUSE = 1

# passo 1: entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chorme')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# demora alguns segundos
time.sleep(5)

# passo2: navegar no sitema e encontrar a base de dados
# (entrar na pasta exportar)
pyautogui.click(x=-1596, y=319, clicks=2)
time.sleep(2)

# Passo 3: exportar/Fazer Download da base de dados
pyautogui.click(x=-1571, y=479)  # clicar no arquivo
pyautogui.click(x=-580, y=198)  # clicar nos 3 pontinhos
pyautogui.click(x=-816, y=631)  # clicar para fazer download
time.sleep(5)

# Passo 4: Importar a base de dados para o python
tabela = pd.read_excel(r'C:\Users\renan alves\Downloads\Vendas - Dez.xlsx')

# Passo 5: Calcular os indicadores
# faturamento - soma da coluna valor final
faturamento = tabela['Valor Final'].sum()

# quantindade - soma da coluna quantidade
quantidade = tabela['Quantidade'].sum()

# Passo 6: Enviar um email para diretoria com o relatório
# abrir email (link: https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(7)

# clicar no escrever
pyautogui.click(x=-1887, y=196)
time.sleep(2)

# escrever email destinatário
pyautogui.write('sanaellysantoss@gmail.com')
pyautogui.press('tab')  # seleciona o destinatario
pyautogui.press('tab')  # passar para o campo de assunto

# escrever assunto
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

# escrever o corpo do email
texto = f'''
Prezados, bom dia

o faturamento de ontem foi de: {faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:.2f}

Abs
Renan Alves
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

# envia o email
pyautogui.click(x=-901, y=742)
