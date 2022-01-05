class Employee:
    company = "Esewa"
    salary = 100

ashish = Employee()
shmita = Employee()
print(ashish.company)
print(shmita.company)
Employee.company = "YouTube"
print(ashish.company)
print(shmita.company)
ashish.salary = 45
print(ashish.salary)

#Below line throws an error as address is not present in class/instance
#print(ashish.address)