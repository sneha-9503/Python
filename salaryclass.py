#Q2).Employee Salary Calculator
#Create an employee class with attribute: Name,Salary and Department.Add a method to give a bonus (Eg:10% of salary).
class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def giveBonus(self):
        bonus = self.salary * 0.10
        bonus=self.salary+bonus
        return bonus
    def display(self):
        print(f"The Employee {self.name} with {self.salary} in {self.department}")
emp1=Employee("Rohit",50000,"Engineering")
emp2=Employee("Suraj",60000,"Accountant")
emp1.display()
print("Bonus for Rohit:", emp1.giveBonus())  
emp2.display()  
print("Bonus for Suraj:", emp2.giveBonus())  

