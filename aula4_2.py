import tkinter as tk
from tkinter import messagebox
def calc_desc():
    try:
        produto = input(entry_produto.get())
        preco = float(entry_preco.get())
        percent = float (preco((preco*percent)/100))
        if imc < 20:
            desconto = "promo comum"
        elif 21 <= imc < 24.9:
            desconto = "boa promo"
        else:
            situacao = "excelente"
        messagebox.showinfo("resultado",f"seu desconto é:{desconto:.2f}\nSituação: {desconto}")
    except ValueError:
        messagebox.showerror("erro","por favor, insira valores validos.")
janela = tk.Tk()
janela.title("calcula desconto")
label_preco = tk.Label(janela,text="preço:")
label_preco.grid(row=0, column=0, padx=10, pady=10)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=0, column=1, padx=10, pady=10)
label_percent = tk.Label(janela,text="desconto:")
label_percent.grid(row=1, column=0, padx=10, pady=10)
entry_percent = tk.Entry(janela)
entry_percent.grid(row=1, column=1, padx=10, pady=10)
label_produto = tk.Label(janela,text="produto:")
label_produto.grid(row=2, column=0, padx=10, pady=10)
entry_produto = tk.Entry(janela)
entry_produto.grid(row=2, column=1, padx=10, pady=10)


botao_calcular = tk.Button(janela, text="calcular desconto", command=calc_desc)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=20)
janela.mainloop()
