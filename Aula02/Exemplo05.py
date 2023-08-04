#leia o valor de um produto, caso seja menor do que 100, mostre a seguinte mensagem
# "Você recebeu 5% de desconto", caso contrário
# "Você recebeu 10% de desconto"

vlr_produto = float(input("informe o valor do produto:"));
if vlr_produto <=0:
    print("valor do produto inválido");

else:
    if vlr_produto <100:
        print("Parabéns você recebeu 5% de desconto");

    else:
        print("você recebeu 10% de desconto:");