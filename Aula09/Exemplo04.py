##Ler a idade de um funcionário e tratar possíveis números negativos. ou valores acima de 130


n_idade = float(input("Informe um valor positivo: "));

if n_idade<0:
    raise ValueError(f"Numero negativo {n_idade} digitado ");

else:
    print("Anão");
