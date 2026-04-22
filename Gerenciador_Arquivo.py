import os
def criar_arquivo():
    nome=input("digite o nome do arquivo (ex:teste.txt):")
    conteudo = input ("digite o conteudo inicial:")
    with open(nome, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print ("arquivo criado com sucesso em:", os.path.abspath(nome))

def ler_arquivo():
    nome = input("digite o nome do arquivo: ")
    if os.path.exists(nome):
        with open(nome, "r", encoding="utf-8") as f:
            print("\nConteudo do arquivo:\n")
            print(f.read())
    else:
        print("arquivo nao encontrado!")

def adicionar_conteudo():
    nome=input("digite o nome do arquivo:")
    if os.path.exists(nome):
        novo=input("digite o conteudo a adicionar:")
        with open(nome, "a", encoding="utf-8") as f:
            f.write("\n" + novo)
        print("conteudo adicionado!")
    else:
        print("arquivo nao encontrado")

def excluir_arquivo():
    nome=input("digite o nome do arquivo:")
    if os.path.exists(nome):
        os.remove(nome)
        print("arquvio excluido com sucesso!")
    else:
        print("arquivo nao encontrado")

def menu():
    while True:
        print("\n=== Gerenciador de arquivos ===")
        print("1 - criar arquivo")
        print("2 - ler arquivo")
        print("3 - adicionar conteudo")
        print("4 - excluir arquivo")
        print("0 - sair")
        opcao = input("escolha uma opcao: ")
        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            ler_arquivo()
        elif opcao == "3":
            adicionar_conteudo()
        elif opcao == "4":
            excluir_arquivo()
        elif opcao == "0":
            print("encerrando...")
            break
        else:
            print("opcao invalida!")

menu()
