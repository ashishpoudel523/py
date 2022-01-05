class person1:
    home = "ktm"

class person2:
    level = "10"

class person3(person1, person2):
    worth = "100 dollar"


p = person3()
print(p.level)

