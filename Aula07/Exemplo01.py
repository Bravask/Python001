# #Trabalhar com estrutura de dados dicionário(dict)

# dados = {};
# print(type(dados));

# alunos ={111:"Karla da silva", 222:"Hélio santos", 333:"Manoel Gomes", 444:"Bruno Mattos"};


# #mostrar primeiro item do dicionário

# print(alunos[111]);

# #Mostrar somente as chaves do Dicionário

# print(alunos.keys());

# #Mostrar somente os valores armazenados no dicionário

# print(alunos.values());

# #Mostra todos os itens do dicionário

# print(alunos.items())

# #Atualizar dicionário

# alunos.update({555:"Paulo Coelho"});

# print(alunos);

# alunos[666] = "Teste";
# print(alunos);
# alunos[111] = "Carlos da Silva";
# print(alunos);

# #Excluir oum item do dicionário
# alunos.pop(666)
# print (alunos)

# #Mostrar somente os valores do dicionário

# for i in alunos.values():
#     print(i)

# #Mostrar somente as chaves do dicionário

# for i in alunos.keys():
#     print(i)

# for i,j in alunos.items():
#     print(i," - ", j);
#     print (i,j, sep=" === ");

dados = {
    'lista_a': [1,2,2,5,8],
    'lista_b': [10,20,30,40],
    'lista_c': [100,200,300,400]
}
print(dados)
print(type(dados))

#Mostrar o ultimo item da lista b

print(dados['lista_b'][-1]);