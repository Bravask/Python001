# #Aula de listas

# lista = [2,8,10,4,55,'coxinha', 34, 'maionese',33];

# print("Primeiro item da lista: ",lista[0]);
# print("Ultimo item da lista: ", lista[-1]);
# print("Penultimo item da lista: ", lista[-2]);
# print("Quantidade de itens da lista: ", len(lista));
# # print("Lista ordenada: ", sorted(lista));

# # --------------------------------------------------------------------------------------------------------------

# pc = ["Mouse", "Monitor", "HD", "Memoria Ram","Camera"];
# print(sorted(pc));
lista = [2,8,10,4,55,'coxinha', 34, 'maionese',33]
lista2 = [6,8,4,11,55,0,3];
pc = ["Mouse", "Monitor", "HD", "Memoria Ram","Camera", "Processador"];
print(sorted(lista2)); # Ordena a lista
print(lista2[2:5]);
lista2.append(1000); # adiciona valor no final da lista
print(lista2);
lista2.insert(2,5000); # adiciona o valor na posição indicada da lista 
print(lista2);
lista2.extend(lista); # unir duas listas
print(lista2);
lista2.pop() #remove o ultimo valor(padrão), mas também remove o valor indicado caso desejar
print(lista2)
lista2.remove("coxinha"); #Remove o valor compativel que esta entre parenteses
print(lista2)
lista3 = pc # valor passado por referência - mexe no pc
lista4 = pc.copy() #copia o objeto, duplica a lista - não mexe no pc se mexer aqui nela
print("Lista 3 ", lista3);
print("Lista 4 ", lista4);
pc.append("SSD")
pc.append("Teclado")
print(lista3);
lista3.append("Placa de video");
print(lista4)
print(pc)