# 2.	Crie um script que leia o nome de 5 alunos e mostre os dados informados em ordem alfabética

alunos = [];
cont = 1;

while cont<=5:
    nome_aluno = input("Digite o nome do Aluno: ");
    alunos.append(nome_aluno);
    cont+=1;
print(sorted(alunos));