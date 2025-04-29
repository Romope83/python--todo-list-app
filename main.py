import tkinter as tk

from controllers.gestor_tarefa import GestorTarefa
from repositories.tarefa_repository import TarefaRepository
from views.tarefa_view import TarefaView

if __name__ == "__main__":
    root = tk.Tk()

    repositorio = TarefaRepository()
    gestor = GestorTarefa(repositorio)
    app = TarefaView(root,gestor)
    
    root.mainloop()
