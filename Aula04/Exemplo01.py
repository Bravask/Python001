#estrutura de repetição while(continuação);
#Leia 5 números e mostra a soma de todos os valores informados

# '''
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# cont = 1;
# soma = 0; #acumulador

# while cont<=5:
#     num = float(input("informe um número: ")); #pede pra digitar 5 vezes
#     soma += num;
#     cont+=1;


# print(f"\nEste é o resultado da soma: {soma:.0f}"); '''
# '''
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #calcular a soma dos valores do intervalo(fechado) das variáveis a e b(280)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# a = 10 #contador inicial
# b = 25 #contador final
# soma = 0 #acumulador

# while a<=b:
#     soma += a; # aqui ele recebe o numero e soma com ele mesmo
#     a +=1; # aqui atualiza o vetor e faz o a que começa com - 10, ficar indo de 1 em 1 até -25

# print(f"\n o Resultado da soma é de: {soma} "); #Aqui mostra o resultado da soma fora do while, por isso ele ta pra esquerda

# #Leia 2 valores e mostre a soma do intervalo entre eles

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# '''

# vlr1 = int(input("Digite um número: ")); # usuário tem que digitar um valor
# vlr2 = int(input("Digite outro numero: ")); #usuário tem que digitar outro valor
# soma = 0

# if vlr1<0 or vlr2<0:
#     print("valor digitado é negativo, por favor digite valores positivos"); #aqui se o cara digitar negativo acaba o codigo

# elif vlr1<vlr2: # aqui ele verifica se o valor1 é menor ele faz a soma a partir do valor1 até o valor2
#     while vlr1<=vlr2:
#         soma += vlr1;
#         vlr1 +=1;

#     print(f"a soma dos valores dentro do intervalo foi de: {soma}"); # mostra a soma

# elif vlr2<vlr1: #aqui ele verifica se o valor 2 é menor  e então ele faz a soma a partir do valor2 até o valor1
#     while vlr2<=vlr1:
#         soma += vlr2;
#         vlr2 +=1;

#     print(f"a soma dos valores dentro do intervalo foi de: {soma}"); #mostra a soma

# else: # aqui se o cara digitar os 2 iguais, ele aparece as mensagens abaixo
#     print("infelizmente não foi possivel somar");
#     print("Verifique os valores informados!");

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# somar 5 valores positivos informados pelo usuario

# soma = 0
# cont = 1
# while cont<=5:
#     nmr_somado = int(input("Digite um número: "));
#     if nmr_somado<0: # se o cara digitar os valores negativos, o codigo fica repetindo, por causa do continue que ignora valores
#         continue
#     soma +=nmr_somado;
#     cont +=1
# print(f"o valor da soma foi de: {soma}");
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# soma = 0
# cont = 1
# while cont<=5:
#     nmr_somado = int(input("Digite um número: "));
#     if nmr_somado>=0: # aqui se digitar positivo, ele fica infinito
#         break
#     soma +=nmr_somado;
#     cont +=1
# print(f"o valor da soma foi de: {soma}");

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#leia 3 notas e mostre a média delas, caso seja digitado um valor negativo ou acima de 10, será solicitado um novo valor

# media_prova = 0
# cont = 1

# while cont<=3:
#     nota_prova = float(input("Digite as notas do aluno: "));
#     if nota_prova<0 or nota_prova>10:
#         continue
#     media_prova +=nota_prova;
#     cont+=1;

# print(f" O valor total da soma foi de: {media_prova}");
# print(f" O valor da soma foi de: {media_prova/(cont-1):.2f}");



                    