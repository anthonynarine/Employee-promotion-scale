class Person:
    
    def __init__(self, first, last):
        print("Constructor is called")
        self.fistname = first
        self.lasname = last

    def fullname(self):
        return f"{self.fistname} {self.lasname}"

class Employee(Person):
    def work(self):
        print(f"employe {self.fullname()} goes to work")

p = Person("Julia", "Narine")
print(p.fullname())
e = Employee("Anthony", "Narine")
print(e.fullname())
print(e.work())


