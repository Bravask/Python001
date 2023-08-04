#Exemplo da função range()
'''
print(list(range(2,15)));
print(list(range(10)));
print(list(range(10,100,5)));
print("*"*100);
#Loop for
for i in range(10):
    print(i, end=" ");

print("\nValor final do contador:",i);
'''
#Contagem de 20 até 30 usando o laço for

# for i in range(20,31):
#     print(i, end= " ");

# #Contagem 10 até zero usando o laço for

# for x in range(10,-1,-1):
#     print("\n",x, end=" ");
# ----------------------------------------------------------------------------------------------------------------------------
#Leia 5 números inteiros e mostre uma mensagem quando o numero for par

# for i in range(0,5):
#     num=int(input("Digite um numero: "));
#     if num%2 ==0:
#         print("O valor informado é par");
#     else:
#         print("o valor informado é impar");

#Leia 5 numeros e some somente os valores impares
# -----------------------------------------------------------------------------------------------------------------------------
# soma = 0
# for i in range(0,5):
#     num1 = int(input("Informe o valor:"));
#     if num1%2 !=0:
#         soma += num1
# print(f"A soma dos numeros impares digitados foi de: {soma}");

# -------------------------------------------------------------------------------------------------------------------
# Leia 5 numeros inteiros e some somente os valores impares e mostre a quantidade de impares
#Mostre a media aritmética dos ímpares
cont=0
soma = 0

for i in range(0,5):
     num1 = int(input("Informe o valor:"));
     if num1%2 !=0:
         soma+= num1;
         cont +=1;


    
print(f"A soma dos numeros impares digitados foi de: {soma}");
print(f"A quantidade de numeros impares digitados foi de: {cont}");
print(f"A media dos impares digitados foi de: {soma/cont:.2f}");



