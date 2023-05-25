
import pyautogui
import time
# pyautogui.click -> clique com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar uma combinação de teclas (ex: Ctrl + D)
# Passo a passomeu_login
pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema da empresa (no link)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

# pode ser que o navegador tenha que carregar
time.sleep(5)

# Passo 2: Fazer login
# clicar no espaço de login
pyautogui.click(x=657, y=371)
# escrever o login
pyautogui.write("meu_login")

# senha
pyautogui.click(x=631, y=462)
pyautogui.write("minha_senha")

# clicar em acessar
pyautogui.click(x=638, y=516)
time.sleep(3)

# Passo 3: Exportar a base de dados
pyautogui.click(x=499, y=362) # clica no arquivo de compras
# pyautogui.click(x=1661, y=198) # clica nos 3 pontinhos
pyautogui.click(x=546, y=580) # faz o download

time.sleep(3)
# Passo 4: Calcular os indicadores
import pandas as pd
caminho_arquivo = R"C:\Users\bia20\Downloads\Compras.csv"
tabela = pd.read_csv(caminho_arquivo, sep=";")
print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

# passo 5: Enviar um e-mail para o meu chefe
# entrar no email: https://mail.google.com/mail/u/0/#inbox
import pyperclip
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=104, y=195)

# preencher as informações do email
# destinatário
pyautogui.write("beatrizpequeno275@gmail.com")
pyautogui.press("tab") # escolher o destinatario

pyautogui.press("tab") # passar para o campo assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # passando para o corpo do email

texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Beatriz Pequeno
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")


# enviar
pyautogui.hotkey("ctrl", "enter")