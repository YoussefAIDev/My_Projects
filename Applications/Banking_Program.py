import time

balance = 0
transactions = []
password = "1234"
is_running = False

print("Welcome to your bank account")
entered = input("Enter your password: ")

if entered == password:
    is_running = True
else:
    print("Wrong password!")
    exit()

def show_balance ():
    print(f"\033[96mYour balance is ${round(balance,2):.2f}\033[0m")

def deposit ():
    amount = float(input("Enter a deposit amount: "))
    if amount < 0:
        print("Thats not a valid amount !")
        return 0
    else:
        print(f"You have deposited ${amount} successfully!")
        transactions.append(f"+${amount}")
        return amount

def withdraw ():
    amount = float(input("Enter a withdraw amount: "))
    if amount > balance:
        print("Error! your balance isnt enough!")
        return 0
    elif amount < 0:
        print("Thats not a valid amount !")
        return 0
    else:
        print(f"You have withdrawed ${amount} successfully!")
        transactions.append(f"-${amount}")
        return amount

def transfer ():
    global balance
    to = input("Enter receiver name: ")
    amount = float(input("Enter amount to transfer: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Not enough balance!")
    else:
        balance -= amount
        print(f"You have transferred ${amount} to {to} successfully!")
        transactions.append(f"Transfer to {to}: -${amount}")

def show_history ():
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        print("Transaction History:")
        for t in transactions:
            print("-", t)

while is_running:
    print("\n\033[95mBanking Program\033[0m")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Withdraw all your money")
    print("5.Transfer")
    print("6.History")
    print("7.Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        show_balance ()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        print(f"You have withdrawed {balance}$ successfully!")
        transactions.append(f"-${balance} (All balance withdrawn)")
        balance = 0
    elif choice == '5':
        transfer()
    elif choice == '6':
        show_history()
    elif choice == '7':
        is_running = False
    else:
        print("Invalid Input! please try again: ")

print("\nExiting", end="")
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print("\nThank you! Have a nice day!")
