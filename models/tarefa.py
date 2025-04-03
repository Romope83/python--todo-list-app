class Tarefa:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_done(self):
        self.completed = True

    def to_dict(self):
        return {"title": self.title, "description": self.description, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        tarefa = Tarefa(data["title"], data["description"])
        tarefa.completed = data["completed"]
        return tarefa
