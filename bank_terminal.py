import sys

class Customer:
    def __init__(this, name, pin):
        this.name = name
        this.pin = pin
        this.balance = 0
    
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
            print("New balance: $" + "%.2f" % this.balance)
        else: print("Insufficient funds")
            
    def deposit(this):
        while(True):
            try:
                amount = float(input("Please enter the amount you would like to deposit: "))
                this.balance += float(amount)
                print("New balance: $" + "%.2f" % this.balance)
                break
            except ValueError:
                print("Please enter a valid number")

print("Please create an account")
name = input("Please enter your name: ")

while(True):
    try:
        pin = (input("Please enter a 4 digit PIN: "))
        if (len(pin) != 4):
            continue
        pin = int(pin)
        break
    except ValueError: continue

customer = Customer(name, pin)

def getPin():
    pinCounter = 0
    while(True):
        pin = (input("Please enter your PIN to access your account: "))
        if (pin != str(customer.pin)):
            pinCounter += 1
            if (pinCounter == 3):
                print("Sorry, too many incorrect tries. Please try again later")
                return False
            print("That's wrong, please try again")
            continue
        break
    return True

def exit():
    print("Exiting...")
    sys.exit()

print("Welcome to the bank!")

if(getPin()):
    while(True):
        selection = input("""Please press the corresponding key to make a selection (ie, press 1 to Display Balance):
                        1. Display Balance
                        2. Make a Withdrawal
                        3. Make a Deposit
                        4. Exit
                        """)
        match(selection):
            case '1':
                customer.displayBalance()
            case '2':
                customer.withdraw()
            case '3':
                customer.deposit()
            case '4':
                exit()
    
        selection = input("Would you like to perform another action? y/n: ")
        if (selection.lower() == 'y'): continue
        exit()

# cust1 = Customer("Mark", 1234, 500)

# cust1.withdraw()