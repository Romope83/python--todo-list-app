from models.tarefa import Tarefa
from repositories.tarefa_repository import TarefaRepository

class GestorTarefa:
    def __init__(self, repositorio:TarefaRepository):
        self.repo = repositorio
        self.tarefas = self.repo.carregar()

    def add_tarefa(self, titulo, descricao=""):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)
        self.repo.salvar(self.tarefas)

    def remove_tarefa(self, titulo):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.titulo != titulo]
        self.repo.salvar(self.tarefas)

    def list_tarefas(self):
        return self.tarefas
