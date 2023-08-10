try:

    txt = open("Aula09/dados.txt","a+");
    print("Arquivo encontrado");
    txt.seek(0);
    print(txt.read())
    
except Exception as e:
    print("Nome do arquivo errado ou não existe");
    print(e);
