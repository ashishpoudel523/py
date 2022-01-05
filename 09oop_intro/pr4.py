class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The squaer of {self.number} is {self.number ** 2}")

    def squareRoot(self):
         print(f"The squaer root of {self.number} is {self.number **0.5}")

    def cube(self):
         print(f"The cube of {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print("Example of static method.")

a1 = calculator(9)
a1.square()
a1.squareRoot()
a1.cube()
a1.greet()