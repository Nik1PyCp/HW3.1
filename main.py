class Student:
    def __init__(self):
        self.name = "Oleg"
        self.surname = "Bobyl"
        self.age = 20
        self.gradebook = [5, 6, 12, 8, 1, 11, 10]
        self.gradebookplus = sum(self.gradebook) / len(self.gradebook)

