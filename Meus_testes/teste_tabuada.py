'''CRIANDO UMA TABUADA'''
import os as cmd
cmd.system('cls');

import entrada_tabuada as enter
import operacao_tabuada as optabuada


print("*" * 50)
print("---------TABUADA VERSÃO 2023----------")
print("*" * 50)

primeira_entrada = input("Aperte qualquer tecla para começar. ")
enter.entrada_tabuada()

verdade_falso = True

while verdade_falso:
    continua_entrada = input("Deseja continuar S/N?\n").strip().upper()

    if continua_entrada == 'N':
        print("Obrigado por usar a tabuada!");
        verdade_falso = False
    elif continua_entrada != 'S':
        print("Entrada digitada incorreta, apenas S/N.");
    else:
        cmd.system('cls');
        enter.entrada_tabuada()


# print("*"*50);
# print("---------TABUADA VERSÃO 2023----------");
# print("*"*50);
# primeira_entrada = input(("Aperte qualquer tecla para começar. "));
# enter.entrada_tabuada()


# continua_entrada = input("Deseja continuar S/N?\n").replace(" ", "").lower();
# verdade_falso = True
# while verdade_falso == True:
#     while continua_entrada == 's':
#         cmd.system('cls');
#         enter.entrada_tabuada()
#         continua_entrada = input("Deseja continuar S/N?\n").replace(" ", "").lower();

#     if continua_entrada == 'n':
#         print("Obrigado por usar a tabuada!");
#         verdade_falso = False;
#     else:
#         continua_entrada = input("Entrada digitada incorreta, por favor digite novamente apenas S ou N: ").replace(" ", "").lower();

