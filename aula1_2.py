def calcular_fatorial(n):
    if n<0:
        return None #
    resultado = 1
    for i in range(1, n + 1):
        resultado *=i
        return resultado

while True:
    try:
        numero = int(input("Digite um número inteiro positivo (ou -1 para sair):"))
        if numero == -1:
            print ("Encerrando o programa. Até logo!")
            break # sai do loop
        elif numero <0:
            print("Erro: o numero deve ser positivo!")
            continue #volta ao inicio do loop
        else:
            fatorial = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é {fatorial}")
    except ValueError:
            print("entrada invalida! Por favor digite um numero inteiro.")
