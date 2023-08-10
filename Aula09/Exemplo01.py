#ler dois números e executar uma divisão dos valores

try:
    n1 = float(input("Digite um numerador: "));
    n2 = float(input("Digite um denominador: "));
    print(f"O resultado da divisão é {n1/n2:.2f}");

except:
    print("Não foi possível realizar a operação");

