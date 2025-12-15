import os 

os.system("cls")

print("Exemplo de tratamento de exceções")
try :
    numero1 = int(input(" Digite um numero :"))
    numero2 = int(input(" Digite um numero :"))


    resultado = numero1 / numero2
    print(f" O resultado da divisão é {resultado}")

except KeyError as erro :
    print(f"Aconteceu o erro {erro}") 
    print("Voce digitou um valor invalido")

