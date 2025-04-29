import tkinter as tk
from tkinter import messagebox
from controllers.gestor_tarefa import GestorTarefa

class TarefaView:
    def __init__(self, root, gestor:GestorTarefa):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        self.tm = gestor

        # Campo de entrada
        self.campo_titulo = tk.Entry(root, width=40)
        self.campo_titulo.grid(row=0, column=0, padx=10, pady=10)

        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.adicionar_tarefa)
        self.botao_adicionar.grid(row=0, column=1, padx=5, pady=10)

        # Lista de tarefas
        self.lista_tarefas = tk.Listbox(root, width=50, height=10)
        self.lista_tarefas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.botao_concluir = tk.Button(root, text="Concluir", command=self.marcar_como_feito)
        self.botao_concluir.grid(row=2, column=0, padx=5, pady=5)

        self.botao_remover = tk.Button(root, text="Remover", command=self.remove_tarefa)
        self.botao_remover.grid(row=2, column=1, padx=5, pady=5)

        self.carregar_tarefas()

    def adicionar_tarefa(self):
        titulo = self.campo_titulo.get()
        if titulo:
            self.tm.add_tarefa(titulo)
            self.carregar_tarefas()
            self.campo_titulo.delete(0, tk.END)

    def carregar_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tm.list_tarefas():
            status = "✅" if tarefa.feito else "❌"
            self.lista_tarefas.insert(tk.END, f"{status} {tarefa.titulo}")

    def marcar_como_feito(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            index = selecionado[0]
            self.tm.tarefas[index].marcar_como_feito()
            self.tm.repo.salvar(self.tm.tarefas)
            self.carregar_tarefas()

    def remove_tarefa(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            index = selecionado[0]
            self.tm.remove_tarefa(self.tm.tarefas[index].titulo)
            self.carregar_tarefas()
