import os

os.system ("cls")
#importa as funções
import funcoes_da_calculadora 

resposta="sim"

while resposta == "sim" :

    os.system("cls")


    print("calculadora com funções")

    numero01 = float(input("Digite o primeiro numero :"))
    numero02= float (input("digite o segundo numero : "))


    #mostrando as opções

   


    opcao = input("Escolha uma opção : ")

    #Verificar a opcao escolhida
    if opcao =="1": 
     print(f"A soma:{funcoes_da_calculadora.somar_com_retorno(numero01,numero02)}")
        
    elif opcao == "2" :
     print(f"A sub: {funcoes_da_calculadora.subtrair_com_retorno(numero01,numero02)}")


    elif opcao == "3" :
        funcoes_da_calculadora.dividir(numero01,numero02)

    elif opcao =="4":
        funcoes_da_calculadora.multiplicar(numero01,numero02)

    elif opcao =="5" :
        funcoes_da_calculadora.calcular_resto_divisao(numero01,numero02)
        
    else : 
        print("opção invalida!") 

    resposta = input ("deseja execultar novamente? sim ou não )").lower()
    
print("programa encerrado com sucesso")
        

