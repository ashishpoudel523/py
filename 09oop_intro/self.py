class Employee:
    company = "Apple"
    def getSalary(self):
        print(f"Salary in {self.company} is {self.salary}")
    
ashish = Employee()



ashish.salary = 20
ashish.getSalary() #Employee.getSalary(ashish) <--THESE ARE SAME-->  

