#Aplicar operadores lógicos com if
#Leia a  qtd de faltas de um aluno e sua média final
#Media é 7 e  mais de 8 faltas reprova
#analisar condição do aluno somente se o valor das faltas for maior ou igual a zero
media_aluno =  float(input("Digite a media do aluno: "));
qtd_faltas = int(input("Digite a quantidade de faltas: "));
print("-"*100);

if qtd_faltas<0 or media_aluno<0:
    print("media ou faltas digitadas incorretamente, digite novamente"); #Primeiro ele verifica se não tem valor negativo

else: 
    if qtd_faltas>8 and media_aluno<7:
        print(f"Aluno reprovado pelos criterios de falta e nota!"); #Aqui ele verifica se o aluno esta reprovado nas faltas EEEEEE na media

    elif qtd_faltas>8: 
        print(f"Aluno reprovado por quantidade de faltas: {qtd_faltas}, superior ao permitido"); #Aluno reprovado por quantidade de faltas
        
    elif media_aluno<7:
        print(f"Aluno reprovado por media baixa: {media_aluno}"); #Aluno reprovado por media
    
    elif media_aluno>10:
        print("Media acima do permitido 10, por favor digite novamente");
    else:
        print("Aprovado"); 

