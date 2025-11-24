
import os 

os.system("cls")

print("""
      
██╗░░░███╗░░░███╗░░░░█████╗░
██║░░░████╗░████║░░░██╔══██╗
██║░░░██╔████╔██║░░░██║░░╚═╝
██║░░░██║╚██╔╝██║░░░██║░░██╗
██║██╗██║░╚═╝░██║██╗╚█████╔╝
╚═╝╚═╝╚═╝░░░░░╚═╝╚═╝░╚════╝░
      """)

nome = input("digite seu nome:")
peso = float (input ("digite seu peso:"))
altura = float (input("digite sua altura "))

imc = peso / (altura * altura )

print(f"Ola {nome}< seu IMC É {round (imc,2)}")

#Abaixo do peso 
if imc <=18.5:
    print ("voce esta abaixo do peso ")

    #peso é  normal 
elif imc >=24.9:
    print ("peso normal ")
    #sobrepeso
elif imc <=29.9:
    print("sobrepeso")
    #obsidade grau 1
elif imc <=39.9:
    print("obsidade grau 2")
else :
    print("obsidade grau 3")    

