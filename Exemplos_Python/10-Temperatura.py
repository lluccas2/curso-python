# Importando a biblioteca os

import os

#limpando a Tela 
os.system("cls")

temperatura = float (input("digite a temperatura em Celsius : "))
if temperatura >= 30 :
    print(" esta quente !")

elif temperatura >=20 :
    print("esta agradavel !")    

elif temperatura >=10 :
    print ("esta frio !")

else :
    print ("esta muito frio !")    
    