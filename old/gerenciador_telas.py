import tkinter as tk

from tela_principal import TelaPrincipal
from tela_login import TelaLogin

class GerenciadorTelas:
    def __init__(self):
        self.janela = tk.Tk()
        self.frame_atual = None
        self.dados_compartilhados = {}
        self.mostrar_tela_principal()
    
    def _mostrar_tela(self, frame_class):
        if self.frame_atual:
            self.frame_atual.destroy()
        
        self.frame_atual = frame_class(self.janela, self)
        self.frame_atual.pack()
    
    def mostrar_tela_login(self):
        self._mostrar_tela(TelaLogin)
    
    def mostrar_tela_principal(self):
        self._mostrar_tela(TelaPrincipal)



app = GerenciadorTelas()
app.janela.mainloop()