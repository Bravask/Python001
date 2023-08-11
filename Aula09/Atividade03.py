import os

nome_arquivo = "Aula09/ArquivoExcluido.txt"

if os.path.exists(nome_arquivo):
    os.remove(nome_arquivo)
    print(f"O arquivo '{nome_arquivo}' foi apagado.")
else:
    print(f"O arquivo '{nome_arquivo}' não existe.")