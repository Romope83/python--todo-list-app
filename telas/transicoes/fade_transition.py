import tkinter as tk


    # uso
    # transicao = FadeTransition(janela1)
    # transicao.fade_in()  # Efeito ao abrir


    # def voltar_tela1():
    # def callback():
    #     janela2.destroy()
    #     criar_tela1()
    # transicao.fade_out(callback)
class FadeTransition:
    def __init__(self, janela):
        self.janela = janela
        self.alpha = 1.0
        
    def fade_out(self, callback):
        self.alpha -= 0.05
        self.janela.attributes('-alpha', self.alpha)
        if self.alpha > 0:
            self.janela.after(30, lambda: self.fade_out(callback))
        else:
            callback()
            
    def fade_in(self):
        self.alpha += 0.05
        self.janela.attributes('-alpha', self.alpha)
        if self.alpha < 1:
            self.janela.after(30, self.fade_in)