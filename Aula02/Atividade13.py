'''
13.	Faça um Script em Python que solicite ao usuário informar o valor de uma compra. Em seguida, 
aplique 10% de desconto e imprima na tela tanto o valor total como também o valor com o desconto aplicado. 
'''
vlr_compra = float(input("Por favor digite o valor da sua compra: "));
vlr_desc = vlr_compra *0.10;
vlr_final = vlr_compra - vlr_desc;
print(f"O valor da sua compra é de {vlr_compra} reais e com desconto de 10% fica em:{vlr_final} reais");