#Estrutura de decisão (Condicionais)

'''
Leia a idade do aluno e defina sua categoria de acordo com as seguintes informações

Categoria - idade
sem categoria - menor do que 3
Infantil - 3 a 10 
Juvenil - 11 até 17
adulto - 18 até 39
senior - 40 até 130
acima de 130 idade inválida
'''

idd_aluno = int(input("Digite a sua idade por favor:"));

if idd_aluno <0:
    print("Idade negativa, digite novamente");

elif idd_aluno < 3:
    print("Idade do aluno sem categoria definida");

elif idd_aluno <=10:
    print("Aluno categoria infantil");

elif idd_aluno <=17:
    print("Aluno categoria Juvenil");

elif idd_aluno <=39:
    print("Aluno categoria adulto");

elif idd_aluno <=130:
    print("Aluno categoria senior");

else:
    print("idade acimda do aceito, por favor digite uma idade válida");

       
