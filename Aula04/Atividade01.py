# 1.	Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente.

num1 = int(input("Digite um numero: "));
num2 = int(input("Digite um numero: "));
if num1>num2:
    while num2<=num1:
        print(num1, end=" ");
        num1 -= 1;
elif num2>num1:
    while num1<=num2:
        print(num2,end= " ");
        num2-=1;
else:
    print("Os numeros são iguais");

