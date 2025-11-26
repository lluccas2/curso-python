import os 

os.system("cls")

print("exemplo - calculado a tabuada")
numero = int (input("digite um numero: "))

#contador ou incremento

i = 10

while (i >=0 ) :
    print(f"{numero} X { i }= { numero * i } ")
    i-=1
print("o programa terminou ")
input ("pressione a tecla <enter> para finalizar... ")    
