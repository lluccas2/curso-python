
import pyautogui
import os
import time
import pyperclip
import webbrowser

os.system("cls")

texto_pesquisa = "Copa do Mundo"

print("Voce tem 5 segundos para posicionar o mouse em algum lugar da tela ")


time.sleep(3)
print(f"Posição atual do mouse :{pyautogui.position()}")

#1 Passo -Abrir o navegador e acessar o site do youtube
webbrowser.open ("https://www.youtube.com/")
time.sleep(3)

#2 Passo - Mover o mouse ate a barra de pesquisa do youtube e clicar 
pyautogui.moveTo(665,98, duration=5)
pyautogui.click(665, 98)

print(" Voce tem 5 segundos para posicionar o mouse em algum lugar na tela ")
time.sleep(3)
print(f" Posição atual do mouse {pyautogui.position}")

# 3 Passo -Digitar  o texto na barra de pesquisa
pyperclip.copy(texto_pesquisa)
pyautogui.hotkey("CTRL", "V")
#pyautogui.write("aulas python")
pyautogui.press("enter")

pyautogui.write("Aulas de python")
pyautogui.press("Enter")

#4 Passo Clicar em um determinado video 
#Scrool para cima = numero positivos
#Scrool para baixo = numero negativos
time.sleep(3)
pyautogui.scroll(-2700)

#5 Passo Mover o mouse ate o video e clicar 
pyautogui.move(1792 ,82 )
pyautogui.click(1792,82)

print("Voce tem 5 segundos para posicionar o mouse em algum lugar")
time.sleep(5)
print(f"Posição atual do mouse: {pyautogui.position()}")

