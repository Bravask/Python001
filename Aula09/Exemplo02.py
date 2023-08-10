
try:
    print(x);

except Exception as coxinha:
    print("Falha ao acessar a variável");
    print(coxinha)

else:
    print("Parabéns!!!! Seu script funcionou perfeitamente!");

finally:
    print("Fim do tratamento de exceções");