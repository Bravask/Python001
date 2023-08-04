#Leia a idade do usuário e informe se ele é maior ou menor de idade


print("--------Bar do Italo para beber aqui tem que ter 18 anos ou mais----------");
idd_pessoa = int(input("informe sua idade por favor:"));

if idd_pessoa <0:
    print("idade inválida");
    print("verifique o valor informado");

elif idd_pessoa >=80:
        print("você já ta velho demais pra beber");
else:
    if idd_pessoa>=18:
        print("Parabéns você é maior de idade, pode beber:");

    else:
        print("não pode beber, você é menor de idade, olha a policia federal");


    
