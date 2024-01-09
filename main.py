class Person:
    def __init__(self, name, age, gender, location, job, farba_oci):
        self.name = name
        self.age = age
        self.gender = gender
        self.__location = location # ak nastavim private dediaci objekt nemoze pouzit tuto hodnotu / pri student funkcii vyhodi chybu
        self.job = job
        self.oci_farba = farba_oci

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"bydlisko je {self.__location}")

    def praca(self):
        print(f"praca je {self.job}")

    def zostarnutie(self, pocet_rokov):
        vek = self.age + pocet_rokov
        print(f"Patrik zostarol o {pocet_rokov} a mas {vek}")

class Student(Person):
    def __init__(self, name, age, gender, location, job, farba_oci, score):# inicializacia pre class Student
        super().__init__(name, age, gender, location, job, farba_oci) # super() sa pouziva na dedenie z nadradenej classy
        self.score = score # pridavam novy

    def jeGenius(self):
        if self.score > 90:
            print(f"{self.name} je genius a {self.gender}")
            print(f"je {self.__location}")
        else:
            print(f"{self.name} nie je genius a {self.gender}")


patrik = Person("Patrik", 30, "muz", "Bratislava", "szco", "modra")
patrik = Student("Patrik", 30, "muz", "Bratislava", "szco", "modra", 100)


patrik.pozdrav()
patrik.bydlisko()
patrik.praca()
patrik.zostarnutie(7)
print(patrik.oci_farba)
patrik.jeGenius()

kamil = Person("Patrik", 30, "muz", "Bratislava", "szco", "modra")
kamil = Student("kamil", 34, "muz", "Bratislava", "IT", "zelena", 150)
kamil.pozdrav()
kamil.bydlisko()
kamil.praca()
kamil.zostarnutie(8)
kamil.jeGenius()

