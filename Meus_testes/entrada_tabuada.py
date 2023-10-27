import operacao_tabuada as optabuada
import os as cmd

def entrada_tabuada():
    while True:
        entrada_numero= input("Digite um número de 1 a 10: ")

        if entrada_numero.isdigit(): # além da função isdigit, tem também a função isaplha() para verificar se foi letra o que foi digitado.
            recebe_inteiro = int(entrada_numero)
            if recebe_inteiro >=1 and recebe_inteiro <=10:
                break
            else:
                print("Por favor digite um número apenas dentro do intervalo de 1 até 10: ");
        else:
            print("Isso não é um número. Tente novamente.")


    entrada_numero= recebe_inteiro # Aqui no final é apenas para estitca minha, colocar o entrada para chamar a função 



    entrada_operacao = input("Escolha qual operação você quer (+, -, *, /):  ").replace(" ","");
    while entrada_operacao != '+' and entrada_operacao != '-' and entrada_operacao != '/' and entrada_operacao != '*': # Aqui ele verifica se o que foi digitado é diferente de tudo isso ai, se for, então executa  a linha, senão ele executa o codigo normalmente
        entrada_operacao = input("Por favor a operação correta ao lado que você quer(+, -, *, /):  ").replace(" ","");
        continue

    optabuada.tabuada(entrada_numero,entrada_operacao);