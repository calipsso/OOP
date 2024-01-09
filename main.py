class Person:
    def __init__(self, name, age, gender, location, job):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.job = job

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"bydlisko je {self.location}")

    def praca(self):
        print(f"praca je {self.job}")

    def zostarnutie(self, pocet_rokov):
        vek = self.age + pocet_rokov
        print(f"Patrik zostarol o {pocet_rokov} a mas {vek}")


patrik = Person("Patrik", 30, "muz", "Bratislava", "szco")
patrik.pozdrav()
patrik.bydlisko()
patrik.praca()
patrik.zostarnutie(7)


kamil = Person("kamil", 34, "muz", "Bratislava", "IT")
kamil.pozdrav()
kamil.bydlisko()
kamil.praca()
kamil.zostarnutie(8)
