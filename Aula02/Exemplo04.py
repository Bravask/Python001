#leia dois números inteiros e mostre somente o menor valor


valor1 = int(input("digite um numero:"));
valor2 = int(input("digite outro numero:")); 


if valor1<valor2:
    print(f"o menor valor informado é o {valor1}");

elif valor2<valor1:
    print(f"O menor valor informado é o {valor2}");

else:
    print(f"os 2 valores são iguais");