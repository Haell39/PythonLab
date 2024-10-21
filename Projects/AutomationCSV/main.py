# çç Instructions:

"""
1. Create/Import a CSV file to VSCode
2. Open browser
3. Access the system site with loguin and password
4. Insert all product info
5. Submit all info to the system
6. Repeat registration until all products are registered

# Passo 1: Entrar no sistema da empresa 
# Passo 2: Fazer login
# Passo 3: Importar a base de produtos pra cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim
"""

import pyautogui
import time
import pandas as pd
import keyboard

# Importing the CSV file
# Passo 3: Importar a base de produtos pra cadastrar
table = pd.read_csv("Projects/AutomationCSV/produtos.csv")
print(table)

# definir o tempo de espera entre cada ação do  PyAutoGUI
pyautogui.PAUSE = 0.6

# abrir sistemas (Brave)
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# wait to load
time.sleep(5)

# loguin in the system
posicao = pyautogui.position()
time.sleep(5)
print(posicao)

pyautogui.click(x=1354, y=343)
pyautogui.write("IqZCZ@example.com")
pyautogui.press("tab")
pyautogui.click(x=1435, y=486)


# Passo 4: Cadastrar um produto

for line in table.index:
    # parando a automação:
    if keyboard.is_pressed("q"):
        print("Ending program...")
        break
    pyautogui.click(x=1810, y=45)
    pyautogui.write(str(table.loc[line, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoqMOLO000251  ria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(table.loc[line, "obs"]):
        pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.click(x=1805, y=53)
    pyautogui.scroll(5000)


# Passo 5: Repetir o processo de cadastro até o fim
