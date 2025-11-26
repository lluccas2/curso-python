import os 

#limpa a tela

os.system("cls")

print("salario do professor")
nivel = input("Qual éo seu nivel ?  \n 1- NIVEL 1 \n 2- NIVEL 2 \n 3- NIVEL 3 \n Digite seu nivel :  ")



qtd_aulas = int(input(" Qual é sua qtd de aulas por semana ?: "))


if nivel =="1":
    salario = (qtd_aulas * 12) *4
elif nivel == "2":
    salario = (qtd_aulas * 17 ) *4   
elif nivel == "3":
    salario =(qtd_aulas *25) *4
else:
    print("o nivel digitado é invalido!")   

#Saida
print (f"O seu salario sera: {salario}")
