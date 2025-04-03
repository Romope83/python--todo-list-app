from tkinter import Tk 

tk = Tk()

class TelaPrincipal(tk.Frame):
    def __init__(self, master, gerenciador):
        super().__init__(master)
        self.gerenciador = gerenciador
        
    def configurar_janela(self):
        
        self.botao.pack(pady=10)
        usuario = self.gerenciador.dados_compartilhados['usuario']
        tk.Label(self, text=f"Bem-vindo, {usuario}").pack()
        tk.Button(self, text="Voltar", 
            command=self.gerenciador.mostrar_tela_login
            ).pack()