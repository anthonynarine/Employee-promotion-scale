class Person:
    
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def info(self):
        print(f"First name: {self.firstname}")
        print(f"last name: {self.lastname}")

class Employee(Person):

    def __init__(self, first, last, employee_id, salary):
        super().__init__(first, last)  #calls the parent class attributes.
        self.employee_id = employee_id
        self.salary = salary

    def info(self):
        super().info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

    def get_raise(self):
        self.salary += 5/100 * self.salary

class LowPerformingEmployee(Employee):
    def get_raise(self):
        self.salary += 1/100 * self.salary

class AveragePerformingEmployee(Employee):
    pass  #average performing employees will get a 5% raise which is  
         #inherited from the parent class Employee

class HighPerformingEmployee(Employee):
    def get_raise(self):
        self.salary += 10/100 * self.salary

p = Person("Julia", "Narine")
e = LowPerformingEmployee("Anthony","Narine", 555, 96000)

print("*" * 25)
e.info()

print("*" * 25)
e.get_raise()
e.info()
print("*" * 25)


