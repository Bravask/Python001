# 4.	Faça um script que leia dois valores positivos e mostre a soma dos números ímpares entre eles.

num1 = int(input("Digite um valor: "));
num2 = int(input("Digite um valor: "));
soma = 0;
if num1<0 or num2<0:
    print("Numeros negativos digitados, por favor digite numero positivos");

elif num1<num2:
    while num1<=num2:
        if num1%2 == 1:
            print(f"{num1}");
            soma += num1;
        num1+=1;
    print(f"A soma dos numeros impares dentro do intervalo é de: {soma}");
elif num2<num1:
    while num2<=num1:
        if num2%2 == 1:
            print(f"{num2}");
            soma +=num2;
        num2+=1;
    print(f"A soma dos numeros impares dentro do intervalo é de: {soma}");
else:
    print("Os números são iguais, não vou contar ");