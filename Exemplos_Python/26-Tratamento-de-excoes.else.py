



try:
    numero = int(input("Digite um numero inteiro : "))
    resultado = 10 / numero

except ZeroDivisionError:
    print ("erro : Não é possivel dividir por zero .")

except  ValueError:
    print ("erro : Voce não digitou um numero valido.")

else:
    #Execulta apenas se  nenhuma excessão tiver ocorrido
    print(f"O resultado da divisão é : {resultado}")

finally:
    #execulta sempre, indepedentemente de erro ou sucesso
    print("Encerrando a operação . . . ")    

