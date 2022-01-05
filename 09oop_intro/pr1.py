class programmer:
    company = "Microsoft"

    def __init__(self, name, age, address):
        self.n = name
        self.a = age
        self.ad = address
        print("Information uploaded.")

    def getDetials(self):
        print(f"company's name is {self.company} , Name is {self.n}, age is {self.a}, address is {self.ad} ")


Anil = programmer("Anil", 21, "KTM")
Ashok = programmer("Ashok", 23, "PKR")


Anil.getDetials()
Ashok.getDetials()


