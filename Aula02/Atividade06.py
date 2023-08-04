'''
6.	Faça um Script em Python que solicite ao usuário informar 3 números. Em seguida, multiplique os valores 
e envie para a saída padrão a seguinte frase: "A multiplicação entre <X>, <Y> e <Z> é igual <Total>". 
'''
num1 = int(input("Por favor digite o 1º numero:"));
num2 = int(input("Por favor digite o 2º numero:"));
num3 = int(input("Por favor digite o 3º numero:"));
mult = num1 * num2 * num3; 
print(f"A multiplicação entre {num1}, {num2} e {num3} é: {mult}");