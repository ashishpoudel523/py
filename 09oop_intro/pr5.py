


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Name is {self.name}")

    def fareInfo(self):
        print(f"price is : {self.fare}")

    def book(self):
        if(self.seats>0):
            print(f"Seats available and seat number is {self.seats}.")
            self.seats = self.seats -1
        else:
            print("Seats not available")

    def cancel(self):
        pass

information = Train("Janakpur Express",  200, 2)
information.getStatus()
information.fareInfo()
information.book()
information.book()
information.book()
