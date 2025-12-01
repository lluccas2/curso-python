import os

#limpa tela

os.system ("cls")

#Função  que exibe o menu 

def exibir_menu():
    print("\n======= Converso de Moedas ====")
    print("[1] converte DOLAR -> REAL")
    print("[2] converte REAL -> DOLAR")
    print("[0] Sair")

#função converter de dolar para real 
def converte_dolar_para_real(quantia_dolar,taxa):

    return quantia_dolar * taxa
#função de real para dolar
def converte_real_para_dolar(quantia_real, taxa):
    return quantia_real / taxa

#função principal do programa     
def main():
    #solicitando a taxa de cambio do dia 
   
    taxa_cambio =float(input(" informe a taxa de cambio"
    "(1 USD = quantos BRL? )"))

    resposta = "sim"
    while resposta =="sim" :
        exibir_menu()
        #solicitando a opção do usuario
        opcao = input("escolha uma opção:")
     
     #verificando a opção escolhida
    if opcao =="1":
        quantia_dolar= float (input("digite a quantia em Dolar( USD) :"))
        total_convertido = converte_dolar_para_real(quantia_dolar,taxa_cambio)
        print(f"USD {quantia_dolar } = R$ {total_convertido}")

    elif opcao =="2":
        valor = float(input("digite o valor em REAL (BRL): "))
        total_convertido = converte_real_para_dolar(quantia_real,taxa_cambio)
        print(f"R${quantia_real} -> USD{total_convertido}")
    elif opcao =="0":
        print("encerrando o programa ... Até mais !")    
    
    else : 
        print("opção invalida ! tente novamente")  

    resposta = input("deseja realizar ou conversão ?(sim / não )")
    
#Chamando a função main 
main()    
