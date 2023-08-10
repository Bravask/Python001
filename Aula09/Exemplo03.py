#Ler a idade de um funcionário e tratar possíveis números negativos. ou valores acima de 130

idade = int(input("Digite a idade: "));

if idade<0 or idade>=130:
    raise Exception("Idade invalida, por favor digite novamente!");

else:
    print(f"Você tem {idade} anos de idade");
