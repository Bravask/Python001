# Lista de nomes de alunos
nomes_alunos = ["Alice", "Bob", "Carol", "David", "Eva"]

# Lista de notas dos alunos
notas_alunos = [
    [8.5, 9.0, 7.8, 9.2],
    [7.6, 8.8, 9.1, 8.2],
    [9.0, 8.7, 8.9, 7.8],
    [6.8, 7.2, 8.5, 7.9],
    [9.5, 9.6, 8.8, 9.1]
]

# Exibir os nomes e notas dos alunos
for i in range(len(nomes_alunos)):
    nome = nomes_alunos[i]
    notas = notas_alunos[i]
    notas_formatadas = " ".join([f"{nota}" for nota in notas])
    print(f"{nome} - {notas_formatadas}")