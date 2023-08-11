#Imagine que você é um desenvolvedor de um aplicativo de registro de vendas. 
# O aplicativo permite que os usuários escrevam o nome a quantidade e valor dos produtos vendidos e 
# salva esses registros em arquivos para que possam ser acessados posteriormente. Seu objetivo é criar um 
# programa simples em Python que simule o funcionamento básico desse aplicativo.

def dados_produto():
    try:
        nome_prodt = input("Digite o nome do produto: "); 

        qtd_prodt = int(input("Digite a quantidade: ")); #nao pode ser menor que zero
        if qtd_prodt<0:
            raise InterruptedError("Quantidade digitada inválida, digite novamente!");
            
        vlr_prodt = float(input("Digite o valor R$: ")); #nao pode ser menor que zero
        if vlr_prodt<0:
            raise InterruptedError("Valor do produto digitado incorretamente, digite novamente!");
            
    except:
        print("Valor digitado incorretamente")
        
    else:
        print("Produto Registrado com sucesso!")
        mensagem = f"\nProduto Registrado: {nome_prodt} com {qtd_prodt} de quantidade e o valor de R${(vlr_prodt):.2f}";
        return mensagem


def cad_produto():
    try:
        txt = open("Aula10/Dados_produto.txt","a+", encoding='utf-8');
        salva = dados_produto()
        txt.write(f"\n{salva}\n");
        txt.close()
    except Exception as e:
        print("Erro ao gravar os dados!!!");    
        print(e)

def ler_dados():
    try:
        txt = open("Aula10/Dados_produto.txt","r", encoding='utf-8');
        txt.seek(0)
        print(txt.read())
        txt.close()
    except Exception as e:
        print("Erro ao ler os dados!!!");    
        print(e)


true = bool
print("*"*150);
print("1 - CADASTRAR PRODUTO");
print("2 - VER PRODUTOS CADASTRADOS");
print("3 - SAIR")
escolha = int(input("Escolha uma Opção:"));
print("*"*150);
while true:
    if escolha == 1:
        cad_produto()
    elif escolha ==2:
        ler_dados()
    elif escolha == 3:
        print("Saindo do aplicativo!");
    break
else:
    print("Opção inválida, por favor tente novamente")
    


