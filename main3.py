class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Department:
    def __init__(self):
        self.workers = []

    def add(self, emp):
        self.workers.append(emp)

    def total_salary(self):
        s = 0
        for w in self.workers:
            s += w.salary
        print(s)


e1 = Employee("Анна", 20000)
d = Department()
d.add(e1)
d.total_salary()
