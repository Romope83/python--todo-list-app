class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False
        self.data_criacao = datetime.now()
        self.data_vencimento = None
        self.prioridade = 0
        self.categorias = []