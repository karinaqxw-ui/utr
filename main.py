class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.done = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def show(self):
        for t in self.tasks:
            print(t.name, t.deadline, t.done)


t1 = Task("Домашка", "12.02")
m = TaskManager()
m.add(t1)
m.show()
