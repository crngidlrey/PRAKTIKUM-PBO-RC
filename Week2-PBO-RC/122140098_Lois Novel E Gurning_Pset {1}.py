import random

class father:
    def __init__(self):
        self.allele = None

    def input_allele(self):
        while True:
            self.show_allele_list()
            allele_input = input("Father's allele: ").upper()
            if allele_input in ['AO', 'AA', 'AB', 'BO', 'BB', 'O']:
                self.allele = allele_input
                break
            else:
                print("Invalid input. Please enter AO, AA, AB, BO, BB, or O.")

    def show_allele_list(self):
        print("Allele list      :")
        print("A homozigot      : AA")
        print("A heterozigot    : AO")
        print("B homozigot      : BB")
        print("B heterozigot    : BO")
        print("AB               : AB")
        print("O                : O\n")

class mother:
    def __init__(self):
        self.allele = None

    def input_allele(self):
        while True:
            self.show_allele_list()
            allele_input = input("Mother's allele: ").upper()
            if allele_input in ['AO', 'AA', 'AB', 'BO', 'BB', 'O']:
                self.allele = allele_input
                break
            else:
                print("Invalid input. Please enter AO, AA, AB, BO, BB, or O.")

    def show_allele_list(self):
        print("Allele list      :")
        print("A homozigot      : AA")
        print("A heterozigot    : AO")
        print("B homozigot      : BB")
        print("B heterozigot    : BO")
        print("AB               : AB")
        print("O                : O\n")

class child(father, mother):
    def __init__(self):
        super().__init__()

    def inherit(self, father, mother):
        father_allele = random.choice(father.allele)
        mother_allele = random.choice(mother.allele)

        if father_allele > mother_allele:
            father_allele, mother_allele = mother_allele, father_allele

        self.allele = father_allele + mother_allele
        print("Child's allele:", self.allele)
        self.bloodtype()

    def bloodtype(self):
        table = {"AA": "A", "AB": "AB", "AO": "A", "BB": "B", "BO": "B", "OO": "O"}

        child_blood_type = table.get(self.allele, "Unknown")
        print("Child's blood type:", child_blood_type)

father = father()
father.input_allele()
print("\n")

mother = mother()
mother.input_allele()
print("\n")

child = child()
child.inherit(father, mother)