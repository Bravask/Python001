#Soma de n valores

def soma_coxinha(*args):
    return sum(args)

def media_valores(*args):
    return sum(args)/len(args)   
def valores (*args):
    return type(args)
def valores_teste(**kwargs): #key words arguments(dicionário parecido)
    return type(kwargs);

if __name__ == '__main__':
    print(media_valores(10,10,10,10,100,10))
    print("="*100)
    print(soma_coxinha(6,10,20,6,7,8,9,20,40,500,210))
    print(media_valores(10,10,10,2))
    print(valores_teste(idade=3, preço=6, qtd=9));