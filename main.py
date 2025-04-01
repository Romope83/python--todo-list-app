import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("400x300")

        self.criar_widgets()

    def criar_widgets(self):
        self.label = ttk.Label(self.root, text="Olá!!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.botao = ttk.Button(self.root, text="Adicionar tarefa", command=self.acao_botao)
        self.botao.pack(pady=10)

    def acao_botao(self):
        print("Botão clicado!")
        self.label.config(text="Você clicou no botão!")

if __name__ == "__main__":
    root = tk.Tk()          # Cria a janela principal
    app = App(root)         # Inicia o app
    root.mainloop()         # Mantém a janela aberta