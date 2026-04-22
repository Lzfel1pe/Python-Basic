estoque = {}
def adicionar_produto():
    """Adiciona um novo produto ao estoque"""
    produto = input("Nome do produto:").strip().title()
    quantidade = int(input("Quantidade inicial:"))
    estoque[produto] = quantidade
    print(f"{produto} adicionado com {quantidade} unidades.")

def ver_estoque():
    """Exibe todos os produtos e quantidades"""
    print("\nEstoque atual:")
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto, quantidade in estoque.items():
            print(f"{produto}:{quantidade}unidades")

def atualizar_quantidade():
    """Atualiza a quantidade de um produto existente"""
    produto = input("Produto a atualizar:").strip().title()
    if produto in estoque:
        nova_qtd = int(input("Nova quantidade:"))
        estoque[produto] = nova_qtd
        print(f"estoque de {produto} atualizado para {nova_qtd}.")
    else:
        print("produto nao encontrado")


def verificar_disponibilidade():
    """Verifica se o produto está disponivel"""
    produto = input("produto a verificar: ").strip().title()
    if produto in estoque:
        if estoque[produto] >0:
            print(f"{produto} está disponível ({estoque[produto]} unidades).")
        else:
            print(f"{produto}está disponível ({estoque[produto]} unidades).")
    else:
        print("produto nao encontrado.")

def menu():
    """Exibe o menu e controla o fluxo principal"""
    while True:
        print("\n===MENU===")
        print("1 - adicionar produto")
        print("2 - ver estoque")
        print("3 - atualizar quantidade")
        print("4 - verificar disponibilidade")
        print("5 - sair")
        opcao = input("escolha uma opção:")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            ver_estoque()
        elif opcao == "3":
            atualizar_quantidade()
        elif opcao == "4":
            verificar_disponibiliade()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválidad! Tente novamente.")

menu()
            
