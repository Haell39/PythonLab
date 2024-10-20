# çç Instructions:

'''
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
'''

import pyautogui
import time
import pandas as pd

# Importing the CSV file
table = pd.read_csv("Projects/AutomationCSV/produtos.csv")
print(table)

# definir o tempo de espera entre cada ação do  PyAutoGUI
pyautogui.PAUSE = 0.6

# abrir sistemas (Brave)
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# wait to load
time.sleep(5)

# loguin in the system

