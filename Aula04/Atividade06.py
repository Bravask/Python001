# 6.	Faça um script em Python para receber dois números informados pelo usuário, mostre o valor da soma de todos os números entre eles e a média dos valores.

num1 = int(input("Digite um valor: "));
num2 = int(input("Digite um valor: "));
soma = 0;
media_vlr = 0
cont = 0
if num1<0 or num2<0:
    print("Numeros negativos digitados, por favor digite numero positivos");

elif num1<num2:
    while num1<=num2:
        print(f"{num1}");
        soma += num1;
        num1+=1;
        cont +=1;
    media_vlr = soma/(cont-1)
    print(f"A soma dos numeros impares dentro do intervalo é de: {soma}");
    print(f"\nA media dos valores digitados é de: {media_vlr:.2f}");

elif num2<num1:
    while num2<=num1:
            print(f"{num2}");
            soma +=num2;
            num2+=1;
            cont +=1;
    media_vlr = soma/(cont-1)
    print(f"A soma dos numeros impares dentro do intervalo é de: {soma}");
    print(f"\nA media dos valores digitados é de: {media_vlr:.2f}");

else:
    print("Os números são iguais, não vou contar ");