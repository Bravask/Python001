#5.	Faça um script que mostre uma sequência numérica iniciando em 63, terminado em 129, calcule e mostre a soma destes valores.

num1 = 63;
num2 = 129;
soma = 0;
while num1<=num2:
    print(num1,end=" ");
    soma +=num1;
    num1+=1;
print(f"\n A soma dos valores foi de {soma}");