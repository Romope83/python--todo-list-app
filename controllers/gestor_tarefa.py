from models.tarefa import Tarefa
from repositories.tarefa_repository import TarefaRepository

class GestorTarefa:
    def __init__(self):
        self.repo = TarefaRepository()
        self.tarefas = self.repo.load()

    def add_tarefa(self, title, description=""):
        tarefa = Tarefa(title, description)
        self.tarefas.append(tarefa)
        self.repo.save(self.tarefas)

    def remove_tarefa(self, title):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.title != title]
        self.repo.save(self.tarefas)

    def list_tarefas(self):
        return self.tarefas
