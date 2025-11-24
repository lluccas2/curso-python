# 1 passo importa a biblioteca os 
import os

#2 passo - utilizar a os para limpar tela
os.system("cls)")

#3 passo realizar as entradas 
nome = input("digite o seu nome: ")

idade = int(input("digite sua idade: "))



#4 verificar a idade  do usuario
if idade >=18 : 
    possui_carteira = input("possui carteira de motorista ? \n (1 - sim\ 2- não ): ")

    if possui_carteira == "1":
        print ("pode dirigir! ")
    else: 
        print ("não pode dirigir ! ")
else :
    print ("menor de idade ")       


