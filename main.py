class Person:
    def __init__(self, name, age, gender, location, job, farba_oci):
        self.__name = name # __ 2x podciarkovnik je private neda sa zmenit, pristupit mozem len zavolanim funkci
        self.age = age # publick viem pristupovat k premennej aj mimo class
        self.gender = gender
        self.location = location
        self._job = job # 1x podciarkovnik je protected
        self.oci_farba = farba_oci

    def pozdrav(self):
        print(f"Ahoj volam sa {self.__name} a mam {self.age} rokov")

    def __bydlisko(self): # Funkcia tiez moze byt private
        print(f"bydlisko je {self.location}")

    def praca(self):
        print(f"praca je {self._job}")

    def zostarnutie(self, pocet_rokov):
        vek = self.age + pocet_rokov
        print(f"Patrik zostarol o {pocet_rokov} a mas {vek}")



patrik = Person("Patrik", 30, "muz", "Bratislava", "szco", "modra")
patrik.name = "Zmena"

patrik.pozdrav()
patrik.__bydlisko()
patrik.praca()
patrik.zostarnutie(7)
print(patrik.oci_farba)


kamil = Person("kamil", 34, "muz", "Bratislava", "IT", "zelena")
kamil.pozdrav()
kamil.bydlisko()
kamil.praca()
kamil.zostarnutie(8)
