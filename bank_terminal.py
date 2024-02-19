import sys

class Customer:
    def __init__(this, name, pin):
        this.name = name
        this.pin = pin
        this.balance = 0
    
    def displayBalance(this):
        print("Current balance: $" + "%.2f" % this.balance)
    
    def withdraw(this):
        while(True):
            try:
                # print selection table, wait for users input
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
                        # get input and store it in amount
                        amount = float((input("Please enter a custom amount: ")))
                        break
                    case _:
                        print("Please enter a valid number")
                        continue
            except ValueError: #ValueError is thrown when user doesn't enter a number (aka float cast didn't work)
                print("Please enter a valid number")

        # after while loop exits, check for sufficient funds
        if (amount < this.balance):
            this.balance -= amount
            print("New balance: $" + "%.2f" % this.balance)
        else: print("Insufficient funds")
            
    def deposit(this):
        while(True):
            try:
                # get input and add it to balance
                this.balance += float(input("Please enter the amount you would like to deposit: "))
                print("New balance: $" + "%.2f" % this.balance)
                break
            except ValueError: # If user enters something that isn't a number, this will trigger
                print("Please enter a valid number")

# Function to validate pin when signing in
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

# Function to exit program
def exit():
    print("Exiting...")
    sys.exit()

# Start of program
print("Please create an account")
name = input("Please enter your name: ")

# PIN loop incase user doesn't input 4 digits
while(True):
    try:
        pin = (input("Please enter a 4 digit PIN: "))
        if (len(pin) != 4): # if pin is less than 4, loop will reset
            continue
        pin = int(pin) # Cast pin to integer
        break
    except ValueError: continue # if pin isn't digits, loop will reset

# create customer's object with their name and pin
customer = Customer(name, pin)

print("Welcome to the bank!")

# run getPin(), if user successfully inputs the pin, start main selection loop. If they fail 3 times, will be False and program will exit
if(getPin()):
    while(True): # Main selection loop
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
else: exit()