programa {
  funcao inicio() {
   //1 passo declarar variavel
   real valor_total
   real porcentagem
   real valor_parte

   //2 passo-entrada
   escreva("digite o primeiro numero")
   leia(valor_total)
   
   escreva("digite o segundo numero")
   leia(porcentagem)
  


   //3 passo-processamento
   valor_parte = valor_total*(porcentagem/100)

   //4 passo- saida 
   escreva("O valor da porcentagem é : ", porcentagem, "% de" , valor_total, "é: ", valor_parte)
   

  
  }
}
