class SmartPhone:
    def __init__(self, name, phoneNum):
        self.owner = name
        self.number = phoneNum

    def printMemberVariavles(self):
        print(f"owner = {self.owner}, phone = {self.number}")


sp1 = SmartPhone("Cho", "010-1111-9999")

sp1.printMemberVariavles()
