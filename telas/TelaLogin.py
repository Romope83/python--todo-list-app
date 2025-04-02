from tkinter import tk

class TelaLogin(tk.Frame):
    def __init__(self, master, gerenciador):
        super().__init__(master)
        self.gerenciador = gerenciador
        
        tk.Label(self, text="Usuário:").pack()
        self.entrada = tk.Entry(self)
        self.entrada.pack()
        
        tk.Button(self, text="Login", 
                command=self.login).pack()
    
    def login(self):
        self.gerenciador.dados_compartilhados['usuario'] = self.entrada.get()
        self.gerenciador.mostrar_tela_principal()