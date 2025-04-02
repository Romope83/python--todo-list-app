import tkinter as tk

class SlideTransition:
    def __init__(self, janela, largura=400, altura=300):
        self.janela = janela
        self.largura = largura
        self.altura = altura
        
    def slide_para_esquerda(self, callback):
        x = self.janela.winfo_x()
        if x > -self.largura:
            self.janela.geometry(f"{self.largura}x{self.altura}+{x-20}+{self.janela.winfo_y()}")
            self.janela.after(10, lambda: self.slide_para_esquerda(callback))
        else:
            callback()
            
    def slide_da_direita(self):
        x = self.largura
        self.janela.geometry(f"{self.largura}x{self.altura}+{x}+{self.janela.winfo_y()}")
        
        def animar():
            nonlocal x
            if x > 0:
                x -= 20
                self.janela.geometry(f"{self.largura}x{self.altura}+{x}+{self.janela.winfo_y()}")
                self.janela.after(10, animar)
        
        animar()