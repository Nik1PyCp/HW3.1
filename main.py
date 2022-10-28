class Student:
    def __init__(self):
        self.name = "Oleg"
        self.surname = "Bobyl"
        self.age = 20
        self.gradebook = [5, 6, 12, 8, 1, 11, 10]
        self.gradebookplus = sum(self.gradebook) / len(self.gradebook)

class Diploma:
    def __init__(self):
        self.diplom = "Диплом"
    def diploma(self):
        if self.gradebookplus > 5:
            print("Я захистив диплом")
        else:
            print("Я не захистив диплом, я пішов на перездачу.")


    def method(self):
        print("about Aspirant")

class Aspirant(Student, Diploma):
    def pr(self):
        self.method()
        print(f"{self.name} "
              f"{self.surname} "
              f"age = {self.age} "
              f"marks = {self.gradebook} "
              f"sum_marks = {self.gradebookplus}")
        self.diploma()

Aspirant1 = Aspirant()
Aspirant1.pr()


