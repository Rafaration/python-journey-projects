import pyautogui
import pandas as pd
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
baseDados = 'produtos.csv'

# passo a passo
# 1: Abrir o navegador
pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

# 2: Acessar o sistema
# entrar no link
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

# Fazer o login
# selecionar o campo do email
pyautogui.click(x=817, y=499)
# Escrever o email
pyautogui.write('Email@email.com')
pyautogui.press('tab')
pyautogui.write('Senha mto dificil')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# 3: Enviar as informações para o sistema
# importar a base de dados

tabela = pd.read_csv(baseDados)

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=883, y=359)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# 4: Repetir o paço 3