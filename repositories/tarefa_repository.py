import json
from models.tarefa import Tarefa

class TarefaRepository:
    CAMINHO_ARQUIVO = "tarefas.json"

    def salvar(self, tarefas):
        with open(self.CAMINHO_ARQUIVO, "w") as f:
            json.dump([tarefa.para_dicionario() for tarefa in tarefas], f)

    def carregar(self):
        try:
            with open(self.CAMINHO_ARQUIVO, "r") as f:
                data = json.load(f)
                return [Tarefa.do_dicionario(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
