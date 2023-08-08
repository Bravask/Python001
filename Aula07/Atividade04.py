# 7.	Crie um script que leia dez números positivos e armazene os dados em uma lista, 
# mostre os dados em ordem crescente, o maior valor informado e menor valor informado.

lista_numeros = [];
cont = 1;

while cont <= 10:
    nmr_digitado = int(input("Digite um numero:"));
    if nmr_digitado<0:
        continue;
    else:
        lista_numeros.append(nmr_digitado);
    cont +=1

print(sorted(lista_numeros));
print("O Maior valor digitado é: ",max(lista_numeros));
print("O Menor valor digitado é: ",min(lista_numeros));