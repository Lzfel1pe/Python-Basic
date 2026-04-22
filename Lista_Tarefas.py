import tkinter as tk
from tkinter import messagebox
tarefas = {}

def adicionar():
    tarefa = entry_tarefa.get()
    if tarefa == "":
        messagebox.showwarning("Aviso", "digite uma tarefa")
        return
    tarefas [tarefa] = "pendente"
    atualizar_lista()
    entry_tarefa.delete(0, tk.END)

def atualizar_lista():
    lista.delete(0, tk.END)
    for tarefa, status in tarefas.items():
        lista.insert(tk.END,f"{tarefa} - {status}")

def concluir():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("aviso","selecione uma tarefa!")
        return
    texto = lista.get(selecionado)
    tarefa = texto.split(" - ")[0]
    tarefas[tarefa] = "concluída"
    atualizar_lista()

def remover():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "selecione uma tarefa")
        return
    texto = lista.get(selecionado)
    tarefa = texto.split(" - ")[0]
    del tarefas[tarefa]
    atualizar_lista()

janela = tk.Tk()
janela.title("lista de tarefas")

tk.Label(janela, text="nova tarefa").pack()
entry_tarefa=tk.Entry(janela,width=40)
entry_tarefa.pack()

tk.Button(janela, text="adicionar", command=adicionar).pack(pady=5)
tk.Button(janela, text="concluir", command = concluir).pack(pady=5)
tk.Button(janela, text="remover", command = remover).pack(pady=5)

lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)

janela.mainloop()
