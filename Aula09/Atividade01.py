# Crie uma função que leia o nome e as notas de um aluno e salve em um arquivo o nome, a média e data do registro.
import datetime

def cad_aluno():
    nome_aluno = input("Digite o nome do aluno: ");
    qtd_notas = int(input("quantas notas serão? "));
    soma_nota=0
    for i in range(qtd_notas):
        nota_aluno = float(input("digite a nota: "));
        if nota_aluno<0 or nota_aluno>10:
            raise ValueError("Numero negativo digitado ");
        else:
            soma_nota+= nota_aluno;
    mensagem = (f"A media do(a) aluno(a): {nome_aluno} foi de: {(soma_nota/qtd_notas):.2f} - Atualização feita :{datetime.datetime.now()}")
    return mensagem

try:
    txt = open("Aula09/RegistroAluno.txt","a+", encoding='utf-8');
    txt.write(f"\n{cad_aluno()}\n");
except Exception as e:
    print("Erro ao gravar os dados!!!");    
    print(e)

else:

    print(txt.read());
    txt.seek(0);
    txt.close();






    