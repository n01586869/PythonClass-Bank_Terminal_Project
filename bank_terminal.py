import math

class Customer:
    def __init__(this, name, pin, balance):
        this.name = name
        this.pin = pin
        this.balance = balance
    
    def displayBalance(this):
        print(this.balance)
    
    def withdraw(this):
        while(True):
            try:
                selection = (input("""
                    Please press the corresponding key to select an option (ie, press 1 to withdraw $20):
                    1. $20
                    2. $40
                    3. $60
                    4. $80
                    5. $100
                    6. Custom amount
                    """))
                match(selection):
                    case '1':
                        amount = 20
                        break
                    case '2':
                        amount = 40
                        break
                    case '3':
                        amount = 60
                        break
                    case '4':
                        amount = 80
                        break
                    case '5':
                        amount = 100
                        break
                    case '6':
                        amount = float((input("Please enter a custom amount: ")))
                        break
                    case _:
                        print("Please enter a valid number")
                        continue
            except ValueError: #ValueError thrown if float cast tries to cast a String. if this occurs, user didn't enter a number
                print("Please enter a valid number")

        # after while loop exits, check for sufficient funds
        if (amount < this.balance):
            this.balance -= amount
            print("New balance: " + str(this.balance))
        else: print("Insufficient funds")
            
    def deposit(this):

        while(True):
            amount = input("Please enter the amount you would like to deposit: ")
            if(amount.isdigit()):
                this.balance += int(amount)
                print("New balance: " + str(this.balance))
                break
            print("Please enter a valid number")

        

cust1 = Customer("Mark", 1234, 500)

cust1.withdraw()