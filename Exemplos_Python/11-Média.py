import os 

os.system ("cls")

print  ("""
     
██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝
      """)

nome = input ("digite o nome do aluno ")
nota01  = float (input("digite a primeira nota : "))
nota02 = float (input("digite a segunda nota: "))
nota03 = float (input ("digite a terceira nota :"))

media = (nota01 + nota02 + nota03) /3

#mostrando a média
print(f" sua media foi {round(media,2)}")

#verificando se o aluno esta aprovado
if media >7:
    print("aprovado")
elif media >4:
    print("recuperação")
else:
    print("reprovado")
input("Pressione <Enter> para fechar o programa.")

