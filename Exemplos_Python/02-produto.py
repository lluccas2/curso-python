
import os
os.system ("cls")
nome_produto =input("digite o nome do produto: ")
preco = float (input("digite o preço do produto: "))
desconto = float (input("digite o porcentual de desconto: "))

#calcular o desconto 
valor_desconto = preco * desconto / 100

#calculando o preço final
preco_final =preco - valor_desconto

#exibir o preco final 
print (f"produto :{nome_produto} - preço final : R$ {preco_final}")