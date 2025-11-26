import os

#limpa tela
os.system("cls")

numero = int(input("digite a idade do nadador: "))

print("Atividade 02 - classificação do nadador")
idade = int (input("digite a idade do nadador "))

#infantil A 5 a 7 
if idade >=5 and idade <7:
    print("infantil A")

elif idade >=8 and idade<=11:
    print("infantil B")

elif idade >=12 and idade <=13:
    print("Juvenil A")

elif idade >=14 and idade <=17:
    print("juvenil B ")

elif idade >18:
    print("Adulto")

else:
    print("A idade invalida")

input(" presssione a tecla <enter> para finalizar ...")
