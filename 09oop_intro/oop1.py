class RailwayForm:
    formType = "Railwayform"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Ashish"
harrysApplication.train = "Nepal Railways"
harrysApplication.printData()
