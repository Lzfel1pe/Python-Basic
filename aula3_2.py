contribuintes = {}
def adicionar_contribuinte():
    nome = input("Nome completo: ").strip().title()
    cpf = input("CPF(somente numeros): ").strip()
    renda = float(input("Renda mensal (R$): "))
    contribuintes [cpf] = {"nome": nome, "renda": renda}
    print(f"{nome} cadastrado com renda de R$ {renda:.2f}.")
def calcular_ir(renda):
    if renda <= 2112:
        return 0
    elif renda <= 2826.65:
        return renda * 0.075 - 158.40
    elif renda <= 3751.05:
        return renda * 0.15 - 370.40
    elif renda <= 4664.68:
        return renda * 0.225 - 651.73
    else:
        return renda * 0.275 - 884.96
def ver_contribuintes():
    print("\n=== lista de contribuintes ===")
    if not contribuintes:
        print("nenhum contribuinte cadastrado")
    else:
        for cpf, dados in contribuintes.items():
            print(f"Nome: {dados['nome']} | CPF: {cpf} | Renda: R$ {dados['renda']:.2f}")
def calcular_ir_contribuintes():
    cpf = input("digite o cpf do contribuinte: ").strip()
    if cpf in contribuintes:
        renda = contribuintes[cpf]["renda"]
        nome = contribuintes[cpf]["nome"]
        imposto = calcular_ir(renda)
        print(f"\nContribuinte: {nome}")
        print(f"Renda mensal: {renda:.2f}")
        print(f"Imposto de renda devido: {imposto:.2f}")
    else:
        print("CPF nao encontrado no sistema")
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. adicionar contribuinte")
        print("2. ver lista de contribuintes")
        print("3. calcular imposto de um contribuinte")
        print("4. sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_contribuinte()
        elif opcao == "2":
            ver_contribuintes()
        elif opcao == "3":
            calcular_ir_contribuintes()
        elif opcao == "4":            
            print("Encerrando o programa...")
            break
        else:
            print("opcao invalida! tente novamente.")
menu()
