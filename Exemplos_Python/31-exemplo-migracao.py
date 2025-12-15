import pyautogui
import time
import webbrowser
import pandas as pd
import os

# --- CONFIGURAÇÕES GLOBAIS ---
# Pequeno atraso entre cada comando para visualização e estabilidade
pyautogui.PAUSE = 0.3 
# Mover o mouse para o canto superior esquerdo (0, 0) interrompe o script
pyautogui.FAILSAFE = True 

# --- DADOS ---
# CORREÇÃO: Usamos os.path.dirname(__file__) para obter o diretório do script
# e garantimos que o arquivo 'clientes.xlsx' seja procurado na mesma pasta.
# Isso resolve o problema de "Current Working Directory".
try:
    # Obtém o caminho completo para o arquivo clientes.xlsx,
    # assumindo que ele está na mesma pasta do script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    EXCEL_FILE_PATH = os.path.join(script_dir, 'clientes.xlsx')
    
    # Carrega a planilha de clientes
    df = pd.read_excel(EXCEL_FILE_PATH)
except NameError:
    # Caso o script seja executado de forma interativa (ex: Jupyter/IDLE), __file__ não existe.
    # Neste caso, voltamos a procurar no diretório de trabalho atual.
    EXCEL_FILE_PATH = 'clientes.xlsx'
    try:
        df = pd.read_excel(EXCEL_FILE_PATH)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{EXCEL_FILE_PATH}' não foi encontrado.")
        print("Certifique-se de que o arquivo está na mesma pasta do script.")
        exit()
except FileNotFoundError:
    print(f"Erro: O arquivo '{EXCEL_FILE_PATH}' não foi encontrado.")
    print("Certifique-se de que o arquivo está na mesma pasta do script.")
    exit()

# --- COORDENADAS DO FORMULÁRIO ---S
# ATENÇÃO: Estas coordenadas são APENAS EXEMPLOS.
# Cada aluno deve encontrar as coordenadas corretas para sua tela (resolução, zoom do navegador, etc.).
# Site de Teste: https://practice.expandtesting.com/register
COORD_URL = 'https://practice.expandtesting.com/register'
COORD_USERNAME = (778, 581) 
COORD_PASSWORD = (777, 695)
COORD_CONFIRM = (789, 786)
COORD_REGISTER = (857, 811)

# --- FUNÇÃO DE AUTOMAÇÃO ---
def preencher_registro(username, password):

    
    # 1. Preencher Username
    pyautogui.moveTo(COORD_USERNAME)
    pyautogui.click()
    pyautogui.write(username)
    time.sleep(3)
    
    # 2. Preencher Password
    pyautogui.moveTo(COORD_PASSWORD)
    pyautogui.click()
    pyautogui.write(password)
    time.sleep(3)

    # 3. Confirmar Password
    pyautogui.moveTo(COORD_CONFIRM)
    pyautogui.click()
    pyautogui.write(password)
    time.sleep(3)

    # 4. Clicar em Registrar
    pyautogui.moveTo(COORD_REGISTER)
    pyautogui.click()
    time.sleep(3)

    # Espera um pouco para o registro ser processado
    time.sleep(2)

#loop principal
print("Iniciando a automação ...")
webbrowser.open((COORD_URL))
time.sleep(5)
print("Voce tem 5 segundo para posicionar o mouse ....")
print (f"posição :{pyautogui.position ()}")




#Execultar a funçaõ preencher para cada resgistro do excel 
for index, linha in df .iterrows():
    
    # 1 Passo pegar os dados da planilha
    username = linha ['usuario']
    password = linha ['senha']

    
    #2 Passo - Chamar a função preencher_registro
    print(f"Processando registro : {username}")
    preencher_registro(username, password)

print("=======================================")
print("Automação concluida ! Todos os registros foram processados")