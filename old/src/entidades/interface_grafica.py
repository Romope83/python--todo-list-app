import tkinter as tk
from tkinter import ttk

class InterfaceGrafica:
    def __init__(self):
        #self.janela_principal = tk.Tk()
        # self.root = tk.Tk()
        
        # self.root.title("Gerenciador de Tarefas")
        # self.root.geometry("400x300")
        # self.configurar_interface()
        # self.root.mainloop() 
        self.tela_inicial()
    def configurar_interface(self):
        self.label = ttk.Label(self.root, text="Olá!!", font=("Arial", 14))
        self.label.pack(pady=10)
        self.botao = ttk.Button(self.root, text="Adicionar tarefa")
        self.botao.pack(pady=10)
    
    def atualizar_lista_tarefas(self):
        # Refresh na exibição das tarefas
        pass
    
    def criar_campo_nova_tarefa(self):
        # Área para digitar novas tarefas
        pass
    
    def criar_lista_visual(self):
        # Componente que mostra as tarefas
        pass
    
    def criar_botoes_controle(self):
        # Botões para ações principais
        pass
    
    def mostrar_mensagem(self, texto):
        # Exibir alertas/confirmações
        pass


    def adicionar_tarefa(self):
        pass    
    def tela_inicial(self):
    # Criar a janela principal
        janela = tk.Tk()
        janela.title("Lista de Tarefas")
        janela.geometry("400x500")

        # Estilo
        cor_fundo = "#f0f0f0"
        cor_botao = "#4CAF50"
        cor_botao_remover = "#f44336"

        janela.configure(bg=cor_fundo)

        # Título
        titulo = tk.Label(janela, text="Minha Lista de Tarefas", font=("Arial", 16, "bold"), bg=cor_fundo)
        titulo.pack(pady=10)

        # Frame de entrada
        frame_entrada = tk.Frame(janela, bg=cor_fundo)
        frame_entrada.pack(pady=10)

        entrada_tarefa = tk.Entry(frame_entrada, width=30, font=("Arial", 12))
        entrada_tarefa.pack(side=tk.LEFT, padx=5)

        botao_adicionar = tk.Button(frame_entrada, text="Adicionar", command=self.adicionar_tarefa, 
                                bg=cor_botao, fg="white", font=("Arial", 10, "bold"))
        botao_adicionar.pack(side=tk.LEFT)

        # Lista de tarefas
        frame_lista = tk.Frame(janela)
        frame_lista.pack(pady=10)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista_tarefas = tk.Listbox(frame_lista, width=50, height=15, font=("Arial", 12), 
                                yscrollcommand=scrollbar.set, selectbackground="#a6a6a6")
        lista_tarefas.pack()

        scrollbar.config(command=lista_tarefas.yview)

        # Botão de remover
        botao_remover = tk.Button(janela, text="Remover Tarefa", command=self.adicionar_tarefa, 
                                bg=cor_botao_remover, fg="white", font=("Arial", 10, "bold"))
        botao_remover.pack(pady=10)

        # Rodapé
        rodape = tk.Label(janela, text="© 2023 Lista de Tarefas", font=("Arial", 8), bg=cor_fundo, fg="gray")
        rodape.pack(side=tk.BOTTOM, pady=10)

        janela.mainloop()        