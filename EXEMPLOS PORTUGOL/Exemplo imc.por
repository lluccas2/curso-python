programa {
  
  inclua biblioteca Matematica --> mat
  
  funcao inicio() {
    //1 passo declarar variaveis

    real peso
    real altura
    real imc

    //2 passo - entrada
    escreva("digite seu peso: ")
    leia(peso)

    escreva("digite sua altura: ")
    leia (altura)

    //3 passo - processamento
    imc= peso / (altura * altura)

    //4 passo - saida 
    escreva(" seu IMC é: ", mat.arredondar(imc,2))
  }

}
