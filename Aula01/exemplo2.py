valor1 = 45
valor2 = 258.45

#operadores aritmeticos + - / * 

#print("soma:", valor1+valor2);
#print("Subtração:", valor1-valor2);
#print("Multiplicação:", valor1*valor2);
#print("Divisão:", valor1/valor2);
#print(f"Divisão com 2 casas decimais: {valor1/valor2:.2f}");
#print(f"valor 2: {valor2:.1f}");

#Obter dados do teclado(Entrada de dados)

#usuario = input("Informe o seu nome:");

#print(f"Seja bem-vindo(a) {usuario}");

#conversão de tipo aqui abaixo V

#idade = int( input("Informe sua idade:"));
#print(f"O nome do usuario é {usuario} e sua idade atual é {idade}");

#mostrar o dobro da idade informada pelo usuario
#print(f"O dobro da idade é:{idade*2}");

#mostrar uma mensagem com 25% do valor do curso
#Parabéns !!! vc ganhou <valor> de credito na proxima compra

Valor_curso = float (input("informe o valor pago no curso:"));

#print(f"Você ganhou desconto de 25% equivalente à {Valor_curso*0.25:.2f} em cima do valor total do curso que é: {Valor_curso} reais");
#print(f"Parabéns!!!, você ganhou {Valor_curso*0.25:.2f} de credito na sua próxima compra");

#solicitar quantidades de parcelas do pagamento

qtd_Parcelas = int(input("Informe a quantidade de parcelas o curso de python:"));
vlr_parcelado = Valor_curso/qtd_Parcelas;
#mostrar o valor das parcelas sem juros
print(f"o curso ficara parcelado em {qtd_Parcelas} vezes de {vlr_parcelado:.2f} reais ");




