#Utilizar para executar comandos cmd

import os
#limpando a tela
os.system("cls")

nome_carro =input("digite o nome do carro: ")
valor_carro =float (input ("digite o valor do carro"))
consumo_por_litro = float (input("digite o consumo por litro: "))
print("----------------------")
print("| carro:", nome_carro  )
print("| valor:", valor_carro )
print("| consumo por litro :" , consumo_por_litro)
print("----------------------------")
