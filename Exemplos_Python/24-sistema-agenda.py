import os

#Lista de Armazenar todos os clientes


dados_clientes = [
    {
        "nome": "Ana Silva",
        "idade": 29,
        "email": "ana.silva@email.com",
        "celular": "(11) 98765-4321"
    },
    {
        "nome": "Bruno Santos",
        "idade": 35,
        "email": "bruno.santos@email.com",
        "celular": "(21) 99876-5432"
    },
    {
        "nome": "Carla Oliveira",
        "idade": 42,
        "email": "carla.oliveira@email.com",
        "celular": "(31) 91234-5678"
    },
    {
        "nome": "Diego Pereira",
        "idade": 27,
        "email": "diego.pereira@email.com",
        "celular": "(41) 92345-6789"
    },
    {
        "nome": "Eduarda Fernandes",
        "idade": 33,
        "email": "eduarda.fernandes@email.com",
        "celular": "(51) 93456-7890"
    }
]







#Função limpa tela 
def limpar_tela():
    os.system("cls")

#Função que exibi o menu na tela 
def exibir_menu():
    print("\n ===== MENU PRINCIPAL ===")
    print('[1] - Cadastro de clientes ')
    print('[2] - Listar clientes Cadastrados')
    print('[3] - Editar Dados de Clientes')
    print('[4] - Excluir um Cliente ')
    print('[5] - Sair do sistema \n')    


#Função  que volta para o menu principal
def voltar_ao_menu_principal():
    input("\n Pressione <ENTER> para voltar ao menu inicial . . . ")
    main()


#Função que cadastra um novo cliente
def cadastrar_novo_cliente():
    try:



        #Solicitando os dados do clientes
        nome =  input("Digite o nome do cliente:")
        idade = input ("Digite a idade do cliente : ")
        email = input ("Digite o email do cliente:")
        celular = input ("Digite o celular do cliente: ")


        #Agrupar os dados do clientes 
        dados_clientes = { 
            'nome ': nome ,
            'idade' : idade ,
            'email' : email,
            'celular': celular      

    }



        #Adicionar o cliente na lista 
        dados_clientes.append(nome)

        #Exibido mensagem de sucesso
        print(f"\n o cliente {nome} foi cadastrado com sucesso!")
    except:
        print ("idade deve ser um numero ")
    finally:
        voltar_ao_menu_principal
#Voltar para o menu principal
#Função que lista todos os clientes cadastrados

def lista_clientes_cadastrados():

    
    #Chamando a função que limpa a tela 
    limpar_tela()    
    print("====LISTA DE CLIENTES CADASTRADOS ====\n ")

    for cliente in dados_clientes:
        print(f"nome:{cliente['nome']} |  | idade : {cliente ['idade']} |  email : {cliente['email']} | celular : { cliente['celular']}")


        #Voltar para menu principal
        voltar_ao_menu_principal()


#Função que exclui um cliente cadastrado
def excluir_cliente():
    limpar_tela()
    print("==== REMOVER CLIENTE===\n")

    indice = 0 

    #Listando os clientes cadastrados
    for indice, cliente in dados_clientes:
        print(f"indice : {indice} | nome:{cliente['nome']} |  | idade : {cliente ['idade']} |  email : {cliente['email']} | celular : { cliente['celular']}")
        indice += 1
    try:
    #Solicitar ao usuario o indice para remover
        indice + int (input ("\n Digite o indice do cliente que deseja remover :"))
        
        if indice >=0 and indice < len (dados_clientes):

    #excluir o cliente escolhido
            cliente_removido = dados_clientes.pop(indice)
            print(f"\cliente{cliente_removido['nome']} removido com sucesso ! ")
        else:
            print("indice invalido")    
            voltar_ao_menu_principal
    except:
        print("Digite um indice valido")
    
    def editar_dados_usuario():
        limpar_tela()
        print("=== EDITAR DADOS DO CLIENTE===\n")
    for indice, cliente in dados_clientes:
            print(f"indice : {indice} | nome:{cliente['nome']} |  | idade : {cliente ['idade']} |  email : {cliente['email']} | celular : { cliente['celular']}")
        
    try:
        indice = int (input ("\n Digite o indice do cliente que deseja remover :"))
            
        if indice >=0 and indice < len (dados_clientes):
            
            #capturar os dados do cliente
            dados_do_cliente = dados_clientes[indice]

            #Exibindo os dados dos clientes selecionado
            print(f"\n Editando os dados do clientes > {dados_do_cliente['nome']}")

            #Solicitando os  novos dados
            novo_nome = input(f"Digite o novo nome (Atual - {dados_do_cliente['nome']}):")
            nova_idade = input (f"Digite a nova idade  (atual {dados_do_cliente['idade']}):")
            novo_email = input(f"Digite o novo e-mail  (Atual -{dados_do_cliente['email']}):")
            novo_celular = input(f"Digite o novo celular  (Atual -{dados_do_cliente['celular']}):")

            #Editar
            dados_do_cliente['nome'] = novo_nome
            dados_do_cliente['idade'] = nova_idade
            dados_do_cliente['email'] = novo_email
            dados_do_cliente['celular'] = novo_celular
                #Função principal do programa
    except :
        print("idade ou indice devem ser validos")
    finally:
        voltar_ao_menu_principal
        
def main():
        limpar_tela()
        print("Bem vindo ao gerenciador de clientes \n")

#Chamar a função que exibe o menu 
exibir_menu()    

#Solicitando uma opção para o usuario
opcao = int(input('escolha uma opção:'))


#Verificando qual foi a opção escolhida

if opcao == 1 :
# Abrir o cadastro de um nive cliente
    cadastrar_novo_cliente()

elif opcao ==2 :
#Abrir a listagem de clientes cadastrados
   lista_clientes_cadastrados()
elif opcao ==3 :
    #Abrir a edição de clientes
    dados_clientes()
   
elif opcao ==4:
    #abrir a exclusão de um cliente 
    excluir_cliente()

elif opcao ==5 :
     exit()

else :
    print ("Opção invalida!")












#Chamando a função principal
main()