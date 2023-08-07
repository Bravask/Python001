# #Criar uma lista de notas

# notas = [6.25, 2,10,9,8.8];

# #Valor máximo de uma nota
# print("O maior valor é:",max(notas));

# #Valor minimo de uma nota
# print("O menor valor é:",min(notas));

# #Quantidade itens na lista de notas
# print("Quantidade de notas:",len(notas));

# #Soma total das notas da lista
# print("Soma das notas:",sum(notas));

# #Media das notas
# print(f"A media é:{sum(notas)/len(notas):.2f} ")

# #Operador in (Booleano: true ou false)
# print(10 in notas);
# # loop for com listas
# print(notas);
# for i in notas:
#     print(i, end=" ");

#leia 5 notas utilizando lista e  estrutura de repetição
# lista = []
# for i in range(5):
#     nmr_digitado = float(input("Digite um numero: "));
#     lista.append (nmr_digitado)

# print("Todas as notas informadas: ",lista);
# print("A quantidade de notas: ", len(notas2));
# print("A soma das notas digitadas é:", sum(notas));

#Leia uma quantidade de notas determinada pelo usuário e faça a soma dos valores digitados

notas = []
cont = 1
qtd_notas = int(input("Digite quantas notas deseja digitar:"));

while cont<=qtd_notas:
    notas_dgtd = float(input("Digite a nota do aluno: "));

    if notas_dgtd<0 or notas_dgtd>10:
        continue
    else:
        notas.append (notas_dgtd);
    cont +=1;

print("a soma total das notas é : ",sum(notas));