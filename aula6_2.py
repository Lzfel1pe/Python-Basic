nome_arquivo = "meu_arquivo.txt"
conteudo = "olá! este é um arquivo  criado com python .\nAprendendo a programar!"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo)
print("arquivo criado com sucesso")
