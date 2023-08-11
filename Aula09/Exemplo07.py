#ler nome e e-mail e aramazenar no arquivos dados3.txt

try:
    txt = open("Aula09/dados3.txt","a+", encoding='utf-8');
    nome = input("Informe o nome: ");
    email = input("input o e-mail: ");
    txt.write(f"{nome:^15} - {email:^15}\n");
except:
    print("Erro ao gravar os dados!!!");
    