import tkinter as tk
from tkinter import messagebox
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = (peso / altura **2)
        if imc < 18.5:
            situacao = "abaixo do peso"
        elif 18.5 <= imc < 24.9:
            situacao = "peso normal"
        elif 25 <= imc <29.9:
            situacao = "sobrepeso"
        else:
            situacao = "obesidade"
        messagebox.showinfo("resultado",f"seu imc é:{imc:.2f}\nSituação: {situacao}")
    except ValueError:
        messagebox.showerror("erro","por favor, insira valores validos.")
janela = tk.Tk()
janela.title("calculadora imc")
label_peso = tk.Label(janela,text="peso(kg):")
label_peso.grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)
label_altura = tk.Label(janela,text="altura(m):")
label_altura.grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)
botao_calcular = tk.Button(janela, text="calcular imc", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=20)
janela.mainloop()

#com base no codigo acima de forma estruturada, simule um programa com tkinter, com as seguintes funcionalidades:
#1- campo p/digitar nome de produto
#2- campo preço original
#3- campo percentual de desconto
#4- ao clicar em calcular desconto, abrir uma cx. de mensagem exibindo nome, preço c/desconto e uma mensagem mostrando o desconto se até 20%(promoçao comum), 21%-49%(boa promo), acimade 50%

