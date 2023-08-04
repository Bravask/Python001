'''
7.	Faça um Script em Python que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie para a saída padrão a média: 
'''
nota1 = float(input("Por favor digite o 1º nota:"));
nota2 = float(input("Por favor digite o 2º nota:"));
nota3 = float(input("Por favor digite o 3º nota:"));
nota4 = float(input("Por favor digite o 4º nota:"));
media = (nota1 + nota2 + nota3 + nota4)/4
print(f"a media final foi de: {media}");