#3.	Faça um script que mostre os números pares em um intervalo definido pelo usuário.

num1 = int(input("Digite um valor: "));
num2 = int(input("Digite um valor: "));
if num1<num2:
    while num1<=num2:
        if num1%2 == 0:
            print(f"{num1}");
        num1+=1;

elif num2<num1:
    while num2<=num1:
        if num2%2 == 0:
            print(f"{num2}");
        num2+=1;

else:
    print("Os números são iguais, não vou contar ");
