class Estilos:
    COR_FUNDO = "#f8f9fa"
    COR_PRIMARIA = "#007bff"
    COR_TEXTO = "#212529"
    FONTE_PADRAO = ("Arial", 12)
    FONTE_TITULO = ("Arial", 16, "bold")
    
    @staticmethod
    def configurar_botao(botao, cor_bg=None):
        botao.configure(
            bg=cor_bg or Estilos.COR_PRIMARIA,
            fg="white",
            font=Estilos.FONTE_PADRAO,
            relief="flat",
            padx=10,
            pady=5
        )