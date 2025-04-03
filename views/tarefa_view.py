import tkinter as tk
from tkinter import messagebox
from controllers.gestor_tarefa import GestorTarefa

class TarefaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        self.tm = GestorTarefa()

        # Campo de entrada
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Adicionar", command=self.add_tarefa)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        # Lista de tarefas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Concluir", command=self.mark_done)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(root, text="Remover", command=self.remove_tarefa)
        self.remove_button.grid(row=2, column=1, padx=5, pady=5)

        self.load_tarefas()

    def add_tarefa(self):
        title = self.title_entry.get()
        if title:
            self.tm.add_tarefa(title)
            self.load_tarefas()
            self.title_entry.delete(0, tk.END)

    def load_tarefas(self):
        self.listbox.delete(0, tk.END)
        for tarefa in self.tm.list_tarefas():
            status = "✅" if tarefa.completed else "❌"
            self.listbox.insert(tk.END, f"{status} {tarefa.title}")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tm.tarefas[index].mark_done()
            self.tm.repo.save(self.tm.tarefas)
            self.load_tarefas()

    def remove_tarefa(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tm.remove_tarefa(self.tm.tarefas[index].title)
            self.load_tarefas()
