#leia um número real e armazene o valor em uma variável

nmr_real = float(input("insira um número aqui:"));


#verificar se o numero é positivo

if nmr_real>0: #teste se for true
    print("o valor informado é positivo");

elif nmr_real==0:
    print("o valor informado é neutro(0)");

else: #teste se for false
    print("o valor informado é negativo:");

print("Aqui finaliza o script!!!");