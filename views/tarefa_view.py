import tkinter as tk
from tkinter import messagebox
from controllers.gestor_tarefa import GestorTarefa

class TarefaView:
    def __init__(self, root, gestor: GestorTarefa):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        frame_botoes = tk.Frame(root)
        frame_botoes.grid(row=1, column=1)
        self.tm = gestor
        self.indice_em_edicao = None

        # Campo de entrada
        self.campo_titulo = tk.Entry(root, width=60)
        self.campo_titulo.grid(row=0, column=0, padx=10, pady=10)

        self.botao_adicionar = tk.Button(root, text="Adicionar", width=15, command=self.adicionar_tarefa)
        self.botao_adicionar.grid(row=0, column=1)

        # Lista de tarefas
        self.lista_tarefas = tk.Listbox(root, width=60, height=10)
        self.lista_tarefas.grid(row=1, column=0)
        self.lista_tarefas.bind("<<ListboxSelect>>", self.ao_selecionar)

        # Botões
        self.botao_concluir = tk.Button(frame_botoes, text="Concluir", width=15, command=self.marcar_como_feito)
        self.botao_concluir.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.botao_concluir.grid_remove()

        self.botao_desconcluir = tk.Button(frame_botoes, text="Desconcluir", width=15, command=self.desmarcar_como_feito)
        self.botao_desconcluir.grid(row=1, column=0, padx=10, pady=(5, 0))
        self.botao_desconcluir.grid_remove()

        self.botao_alterar = tk.Button(frame_botoes, text="Alterar", width=15, command=self.preparar_alteracao)
        self.botao_alterar.grid(row=2, column=0, padx=10, pady=(5, 0))
        self.botao_alterar.grid_remove()

        self.botao_remover = tk.Button(frame_botoes, text="Remover", width=15, command=self.remove_tarefa)
        self.botao_remover.grid(row=3, column=0, padx=10, pady=(5, 0))
        self.botao_remover.grid_remove()

        self.botao_salvar = tk.Button(frame_botoes, text="Salvar", width=15, command=self.salvar_alteracao)
        self.botao_salvar.grid(row=4, column=0, padx=10, pady=(5, 0))
        self.botao_salvar.grid_remove()

        self.botao_cancelar = tk.Button(frame_botoes, text="Cancelar", width=15, command=self.cancelar_alteracao)
        self.botao_cancelar.grid(row=5, column=0, padx=10, pady=(5, 10))
        self.botao_cancelar.grid_remove()

        self.carregar_tarefas()
        self.root.resizable(False, False)

    def atualizar_botoes(self, estado):
        selecionado = self.lista_tarefas.curselection()
        tarefa_feita = False
        
        if selecionado:
            index = selecionado[0]
            tarefa_feita = self.tm.tarefas[index].feito

        if estado == "normal":
            # Oculta ambos inicialmente
            self.botao_concluir.grid_remove()
            self.botao_desconcluir.grid_remove()
            
            # Mostra apenas o botão relevante
            if selecionado:
                if tarefa_feita:
                    self.botao_desconcluir.grid()
                else:
                    self.botao_concluir.grid()
                
                self.botao_alterar.grid()
                self.botao_remover.grid()

            self.botao_salvar.grid_remove()
            self.botao_cancelar.grid_remove()
            
        elif estado == "edicao":
            self.botao_concluir.grid_remove()
            self.botao_desconcluir.grid_remove()
            self.botao_alterar.grid_remove()
            self.botao_remover.grid_remove()
            self.botao_salvar.grid()
            self.botao_cancelar.grid()


    def ao_selecionar(self, event):
        if not self.indice_em_edicao:
            self.atualizar_botoes("normal")

    def carregar_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tm.list_tarefas():
            status = "✅" if tarefa.feito else "❌"
            self.lista_tarefas.insert(tk.END, f"{status} {tarefa.titulo}")

    def adicionar_tarefa(self):
        titulo = self.campo_titulo.get().strip()
        if titulo:
            self.tm.add_tarefa(titulo)
            self.carregar_tarefas()
            self.campo_titulo.delete(0, tk.END)

    def marcar_como_feito(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            index = selecionado[0]
            self.tm.tarefas[index].marcar_como_feito()
            self.tm.repo.salvar(self.tm.tarefas)
            self.carregar_tarefas()
            self.atualizar_botoes("normal")

    def desmarcar_como_feito(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            index = selecionado[0]
            self.tm.tarefas[index].feito = False
            self.tm.repo.salvar(self.tm.tarefas)
            self.carregar_tarefas()
            self.atualizar_botoes("normal")

    def remove_tarefa(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            index = selecionado[0]
            self.tm.remove_tarefa(self.tm.tarefas[index].titulo)
            self.carregar_tarefas()

    def preparar_alteracao(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            self.indice_em_edicao = selecionado[0]
            tarefa = self.tm.tarefas[self.indice_em_edicao]
            self.campo_titulo.delete(0, tk.END)
            self.campo_titulo.insert(0, tarefa.titulo)
            self.atualizar_botoes("edicao")

    def salvar_alteracao(self):
        if self.indice_em_edicao is not None:
            novoTitulo = self.campo_titulo.get().strip()
            if novoTitulo:
                tarefa = self.tm.tarefas[self.indice_em_edicao]
                tarefa.titulo = novoTitulo
                self.tm.repo.salvar(self.tm.tarefas)
                self.carregar_tarefas()
                self.cancelar_alteracao()

    def cancelar_alteracao(self):
        self.indice_em_edicao = None
        self.campo_titulo.delete(0, tk.END)
        self.atualizar_botoes("normal")
        self.lista_tarefas.selection_clear(0, tk.END)