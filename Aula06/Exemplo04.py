#Tupla

# cidades = ('Manaus','Coari', 'Parintins','Manacapuru', 'Anori');

# #Mostrar o ultimo item da tupla
# print("Ultimo item: ", cidades[-1]);

# #Mostrar o primeiro item da tupla
# print("Primeiro item:", cidades[0]);

# #Mostrar os itens ordenados
# print("Aqui é a tupla ordenada: ",sorted(cidades));

# print(cidades.count('Manaus'));

#Leia 3 numeros positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e menor valor informado.

nmr_lista= [];
cont = 1;

while cont<=3:
    nmr_digitado = int(input("Digite um valor: "));

    if nmr_digitado<0:
        continue
    else:
        nmr_lista.append(nmr_digitado);
    
    cont +=1

print(f"Os valore em ordem crescente é: {sorted(nmr_lista)}");
print(f"O maior valor digitado  é: {max(nmr_lista)}");
print(f"O maior valor digitado  é: {min(nmr_lista)}");