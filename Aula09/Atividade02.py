# Crie uma função que leia o nome do curso, carga horária e valor e registre em um arquivo.

def cad_curso():
    nome_curso = input("Nome do curso: ");
    carga_hor = int(input("Qual a carga horária? "));
    vlr_curso = float(input("Qual o  valor do curso R$? "));
    mensagem = (f"O nome do curso é {nome_curso}, com a carga horária de: {carga_hor} horas e no valor de R${(vlr_curso):.2f} reais");

    return mensagem

try:
    txt = open("Aula09/RegistroCurso.txt","r", encoding='utf-8');

except Exception as e:
    print("Erro ao gravar os dados!!!");    
    print(e)

else:
    print(txt.read());
    txt.seek(0);
    txt.close();