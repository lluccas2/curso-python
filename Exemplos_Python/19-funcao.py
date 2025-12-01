import os

#limpa tela

os.system ("cls")

#exemplo de função sem parametros

def escreva():
    print("bem vindo ao sistema")

    #exemplo de função com parametros
def exibir_idade(suaidade,nome):
    print(f"seu nome {nome} tem {suaidade}anos!")
def somar(n1,n2):
    resultado =n1+n2 
    print(f"o resultado é : {resultado}")   

#exemplo de função com retorno
def subtrair(valor1 , valor2):
    resultado = valor1 - valor2 
    return resultado 

print("execultou programa")

 #chamando uma funçao sem paramentros
escreva()

    #chamando uma funçao com parametros
exibir_idade(24, "Juliannee ")
exibir_idade(28, "Lucas ") 
somar(50,90)

#chamando uma função com retorno
total =subtrair (5,2)
total2 = somar (3,5)


