import random


class IanFirstBank:
    def __init__(self, name, age, balance, accountNumber, phone):
        self.name = name
        self.age = age
        self.balance = balance
        self.accountNumber = accountNumber
        self.phoneNumber = phone

    def deposit(self, amount):
        self.balance += amount

        print("you have " + str(self.balance) +"$")

    def withdraw(self, amount):
        self.balance -= amount
        print("you have " + str(self.balance) +"$")

    def checkBalance(self):
        print("you have " + str(self.balance) +"$")

account_1 = IanFirstBank("Bob", 45, 300, "124ab34", "NA")
account_2 = IanFirstBank("Sally", 25, 100, "154av34", "NA")

account_1.checkBalance()
account_1.deposit(500)
account_1.withdraw(150)

account_2.checkBalance()
account_2.deposit(200)
account_2.withdraw(50)

bankUsers = []

def CreateAccount():
    print("Welcome to Ian's First Bank")
    print("Please fill out the following information to create your account")
    name = input("Please type in your name: ")
    age = int(input("Please type in your age: "))
    balance = int(input("Please type in how much you want to deposit: "))
    accountNumber = random.randrange(100,500)

    print("Congrats! Your account has been created")

    account_1 = IanFirstBank(name, age, balance, accountNumber, "NA")
    bankUsers.append(account_1)
    return account_1
print(bankUsers)



def mainBankApp():
    print("Welcome")
    print("Are you a new user?")
    print("Please type 1 for existing user or 2 for new user")
    answer = int(input())
    if answer == 1:
        print("Welcome back")
    elif answer == 2:
        CreateAccount()