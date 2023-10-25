'''CRIANDO UMA TABUADA'''
import os as cmd

cmd.system('cls');

def tabuada(numero, operador):
    operacao_escolhida = operador;
    numero_escolhido = numero;
    contador = 1;
    resultado = 0;
    if operacao_escolhida == '+':
        
        while contador <=10:
            resultado = contador + numero_escolhido;
            print(f"{contador} + {numero_escolhido} = {resultado}");
            contador +=1;
    
    if operacao_escolhida == '*':
        
        while contador<=10:
            resultado = contador * numero_escolhido;
            print(f"{contador} * {numero_escolhido} = {resultado}");
            contador +=1;

    if operacao_escolhida == '-':

        num_subtraido = numero_escolhido +1; #Não entendo o porque disso aqui funcionar, mas resolve o problema;
        while contador <= 10: 
            resultado =  num_subtraido- numero_escolhido;
            print(f"{num_subtraido} - {numero_escolhido} = {resultado}");
            num_subtraido +=1;  # Aqui ele vai subindo o numero subtraido pelo escolhido até chegar no fim;
            contador +=1;
    
    if operacao_escolhida == '/':

        while contador <= 10:
            dividendo = contador * numero_escolhido; 
            resultado = dividendo / numero_escolhido;
            print(f"{dividendo:.0f} / {numero_escolhido} = {resultado:.0f}");
            contador +=1;
            


print("*"*50);
print("---------TABUADA VERSÃO 2023----------");
print("*"*50);

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



entrada_operacao = input("Escolha qual operação você quer: +, -, *, /\n").replace(" ","");
while entrada_operacao != '+' and entrada_operacao != '-' and entrada_operacao != '/' and entrada_operacao != '*': # Aqui ele verifica se o que foi digitado é diferente de tudo isso ai, se for, então executa  a linha, senão ele executa o codigo normalmente
    entrada_operacao = input("Por favor a operação correta ao lado que você quer: +, -, *, /\n").replace(" ","");
    continue

tabuada(entrada_numero,entrada_operacao);