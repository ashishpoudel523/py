class Vehicle:
    def info(self):
        print("Moves on road.")

class Car(Vehicle):
    def a(self):
        print("Green Color")

class bike(Car):
    def b(self):
        print("Two wheels")

b = bike()
b.info()
b.a()
b.b()