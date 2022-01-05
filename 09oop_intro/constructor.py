class student:
    
    #self or aru j sukai lekhda ni hunxa
    def __init__(self, age, salary, name):
        self.age = age
        self.salary = salary
        self.name = name
        print("Employee is created")

    def getDetials(self):
        print(f"Name is {self.name}, salary is {self.salary}, age is {self.age}.")
ashish = student(21, 100, "Ashish")

ashish.getDetials()

