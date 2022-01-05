class mother:
    place = "Nepal"

    def do(self):
        print("Eat food.")

class child(mother):
    work = "food cook"

    def inHome(self):
        print(f"She works all day and {self.work}")

    def takeBreak(self):
        print("She takes rest.")

class dad(mother):
    company = "Facebook"

    def inHome(self):
        print("No work at home.")

m = mother()
m.do()
c = child()
d = dad()
print(d.place)