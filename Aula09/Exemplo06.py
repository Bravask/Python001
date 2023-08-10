# Abertura de um arquivo chamado dados2.txt
# Ler o nome de 10 pessoas e gravar no arquivo

try:
        txt=open("Aula09/dados2.txt","w+"); # w - (grava por cima) a+ - (adiciona sem gravar por cima)
        for i in range(10): # não é pra abrir o arquivo várias vezes, só uma e digitar os dados e depois fechar
            nome_pessoa = input("Digite seu nome: ");
            txt.write(f"\n {i+1} - Nome: {nome_pessoa}\n");
        
except:
    print("Erro 404 not Found");

else:
    txt.seek(0);
    print(txt.read())
    txt.close()