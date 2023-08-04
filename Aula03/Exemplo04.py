"""
cont = 0

while cont<=100:
    print(cont, end=" ");
    cont = cont+1;

print("\nvalor final do contador: ", cont)

#Contagem iniciando em 50 até 200

cont2 = 50
print("-"*100)

while cont2<=200:
    print(cont2, end=" ");
    cont2 +=1

print("\n valor final do contador 2: ", cont2);

print("-"*100)

#Contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10

cont3 = 10

while cont3<=80:
    print(cont3, end=" ");
    cont3 +=10

print("\n valor final do contador 3: ", cont3);

print("-"*100);

#Mostrar a mensagem "Eu tenho que estudar" *300

cont4 = 1

while cont4<=300:
    print(f"{cont4} - Eu tenho que estudar");
    cont4 += 1

print("-"*100);


#Leia um número e mostre a contagem a partir de zero até o número informado.


cont = 0 
i = int(input("Digite um valor: "));

while cont<=i:
    print(cont, end=" ");
    cont +=1

print("\n O valor final foi de", cont); 
"""
#Contagem decrescente iniciando em 23 até 0
'''
cont=23

while cont>=0:
    print(cont, end=" ");
    cont -= 1;

print("\nvalor final",cont);
'''

#leia 2 numeros e mostre a contagem do intervalo dos valores informados

num1 = int(input("Digite o valor inicial da contagem: "));
num2 = int(input("Digite o valor final da contagem: "));

if num1<0 or num2<0:
    print("numeros negativos digitado, por favor digite numeros acima de 0");

else:
    if num1<num2:
        while num1<=num2:
            print(num1, end=" ");
            num1 +=1;

    elif num2<num1:
        while num2<=num1:
            print(num2, end=" ");
            num2 +=1;
    else:
        print("valores iguais não irei contar");
