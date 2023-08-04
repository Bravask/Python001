#Primeiro script em Python

print("Hello World!!!");
print("Curso Programando com python!");
print("-"*20);
print("Carga horária: 40 horas \n10 dias");
Nome_Pessoa = "Italo Brito"
Idade_Pessoa = 24
Valor_Curso = 249.99
Nome_Curso =  "Programando com Python"

#Mostrar tipos de dados  das variáveis
print(type(Nome_Pessoa));
print(type(Idade_Pessoa));
print(type(Valor_Curso));

#Concatenar dados

print("Seja bem-vindo(a)",Nome_Pessoa);
print("Seja bem-vindo(a)",Nome_Pessoa, "ao curso:",Nome_Curso);

#o Curso <Nome_Curso> custa <valor>

print("O curso",Nome_Curso,"custa exatamente:",Valor_Curso,"Reais");

#f-strings no python

print(f"Seja bem-vindo {Nome_Pessoa} ao curso {Nome_Curso} que custa {Valor_Curso} ");