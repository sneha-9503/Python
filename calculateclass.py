#Q1).Create the calculator class with methods to perform basic arithmetic operations such as addition,subtraction,multiply and divide.
class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b."""
        return a / b
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c = Calculator()
print("Addition:", c.add(a, b))         
print("Subtraction:", c.subtract(a, b))  
print("Multiplication:", c.multiply(a, b)) 
print("Division:", c.divide(a, b))        
