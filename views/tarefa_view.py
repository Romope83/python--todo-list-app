import tkinter as tk
from tkinter import messagebox
from controllers.gestor_tarefa import GestorTarefa

class TarefaView:
    def __init__(self, root, gestor:GestorTarefa):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        frame_botoes = tk.Frame(root)
        frame_botoes.grid(row=1, column=1)
        self.tm = gestor
        self.indice_em_edicao = None  # novo

        # Campo de entrada
        self.campo_titulo = tk.Entry(root, width=60)
        self.campo_titulo.grid(row=0, column=0, padx=10, pady=10)

        self.botao_adicionar = tk.Button(root, text="Adicionar",width= 15, command=self.adicionar_tarefa)
        self.botao_adicionar.grid(row=0, column=1)

        self.botao_salvar = tk.Button(root, text="Salvar",width=15, command=self.salvar_alteracao)
        self.botao_salvar.grid(row=0, column=1)    
        self.botao_salvar.grid_remove()    

        # Lista de tarefas
        self.lista_tarefas = tk.Listbox(root, width=60, height=10)
        self.lista_tarefas.grid(row=1, column=0)
        self.lista_tarefas.bind("<<ListboxSelect>>", self.ao_selecionar)
        self.lista_tarefas.bind("<FocusOut>", self.ao_perder_foco)

         #Botões
        self.botao_concluir = tk.Button(frame_botoes, text="Concluir",width=15, command=self.marcar_como_feito)
        self.botao_concluir.grid(row=0, column=0,padx=(10,10),pady=(10,0))
        self.botao_concluir.grid_remove()  

        self.botao_alterar = tk.Button(frame_botoes, text="Alterar",width=15, command=self.preparar_alteracao)
        self.botao_alterar.grid(row=1, column=0,padx=(10,10),pady=(20,0))
        

        self.botao_remover = tk.Button(frame_botoes, text="Remover",width=15, command=self.remove_tarefa)
        self.botao_remover.grid(row=2, column=0,padx=(10,10),pady=(20,0))
        #self.botao_remover.grid_remove()

        self.botao_cancelar = tk.Button(frame_botoes, text="Cancelar",width=15, command=self.cancelar_alteracao)
        self.botao_cancelar.grid(row=3, column=0,padx=(10,10),pady=(20,10))

        self.carregar_tarefas()


        self.root.resizable(False, False)
        self.alterar_funcao("iniciar")



    def alterar_funcao(self,estado):
        match estado:
            case "iniciar":
                self.botao_salvar.grid_remove()
                self.botao_alterar.grid_remove()
                self.botao_concluir.grid_remove()                            
                self.botao_remover.grid_remove()      
                self.botao_cancelar.grid_remove()                        
            case "selecionar_item":
                self.botao_salvar.grid_remove()
                self.botao_alterar.grid()
                self.botao_concluir.grid()                           
                self.botao_remover.grid() 
            case "alterar":
                self.botao_salvar.grid()
                self.botao_alterar.grid_remove()
                self.botao_concluir.grid_remove()                            
                self.botao_remover.grid_remove()      
                self.botao_cancelar.grid() 
            case _:
                return "Dia comum!"
            
    def ao_selecionar(self,event):
        self.alterar_funcao("selecionar_item")

    def ao_perder_foco(self,event):
        self.alterar_funcao("iniciar")
                    
    def carregar_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tm.list_tarefas():
            status = "✅" if tarefa.feito else "❌"
            self.lista_tarefas.insert(tk.END, f"{status} {tarefa.titulo}")

    def adicionar_tarefa(self):
        titulo = self.campo_titulo.get().strip()
        if titulo:
            self.lista_tarefas.insert(tk.END, f"[ ] {titulo}")
            self.campo_titulo.delete(0, tk.END)

    def marcar_como_feito(self):
        sel = self.lista_tarefas.curselection()
        if sel:
            idx = sel[0]
            texto = self.lista_tarefas.get(idx)
            if texto.startswith("[ ]"):
                self.lista_tarefas.delete(idx)
                self.lista_tarefas.insert(idx, texto.replace("[ ]", "[X]", 1))

    def remove_tarefa(self):
        sel = self.lista_tarefas.curselection()
        if sel:
            self.lista_tarefas.delete(sel[0])

    def preparar_alteracao(self):
        sel = self.lista_tarefas.curselection()
        if sel:
            idx = sel[0]
            texto = self.lista_tarefas.get(idx)
            titulo = texto[4:]  # remove o "[ ] " ou "[X] "
            self.campo_titulo.delete(0, tk.END)
            self.campo_titulo.insert(0, titulo)
            self.indice_em_edicao = idx
            self.alterar_funcao("alterar")

    def salvar_alteracao(self):
        if self.indice_em_edicao is not None:
            novo_texto = self.campo_titulo.get().strip()
            if novo_texto:
                antigo = self.lista_tarefas.get(self.indice_em_edicao)
                prefixo = "[X]" if "[X]" in antigo else "[ ]"
                self.lista_tarefas.delete(self.indice_em_edicao)
                self.lista_tarefas.insert(self.indice_em_edicao, f"{prefixo} {novo_texto}")
                self.cancelar_alteracao()

    def cancelar_alteracao(self):
        self.campo_titulo.delete(0, tk.END)
        self.indice_em_edicao = None
        self.botao_salvar.grid_remove()
        self.botao_cancelar.grid_remove()

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
