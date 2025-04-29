class Tarefa:
    def __init__(self, titulo, descricao=""):
        self.titulo = titulo
        self.descricao = descricao
        self.feito = False

    def marcar_como_feito(self):
        self.feito = True

    def para_dicionario(self):
        return {"titulo": self.titulo, "descricao": self.descricao, "feito": self.feito}

    @staticmethod
    def do_dicionario(data):
        tarefa = Tarefa(data["titulo"], data["descricao"])
        tarefa.feito = data["feito"]
        return tarefa
