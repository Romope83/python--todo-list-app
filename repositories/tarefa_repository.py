import json
from models.tarefa import Tarefa

class TarefaRepository:
    FILE_PATH = "tarefas.json"

    def save(self, tarefas):
        with open(self.FILE_PATH, "w") as f:
            json.dump([tarefa.to_dict() for tarefa in tarefas], f)

    def load(self):
        try:
            with open(self.FILE_PATH, "r") as f:
                data = json.load(f)
                return [Tarefa.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
