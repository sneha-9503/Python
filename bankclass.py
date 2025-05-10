#Q4).Bnak Account Simulation
#Create a class BankAccount with deposit,withdraw and checkBalance functionalities.Prevent withdrawal if balance is insufficient.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=  self.balance+amount
        print(f"Deposited amount: ${amount}")
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance=self.balance-amount
            print(f"Withdraw amount: ${amount}")
        else:
            print("Balance is insufficient")
    def checkBalance(self):
        return self.balance
name=input("Enter the name:")
balance=int(input("Enter the balance:"))
bank=BankAccount(name,balance)
print("Current Balance: $",bank.checkBalance())
bank.deposit(500)
bank.withdraw(200)
print("Current Balance:$",bank.checkBalance())
bank.withdraw(1500)

