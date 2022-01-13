print("********************\nATM System\n********************")

print("""
Transactions:

1. Balance .ınquiry
2. Deposit Money
3. Withdraw Money

You can exit the program by typing 'quit'.

""")

balance  = 1000 # Let's say our balance is $1000.

while True:
    process = input("Enter the action you want to do:")

    if (process == "quit"):
        print("Thank you.")
        break
    elif (process == "1"):
        print("Your balance {} is dollars".format(balance))
    elif (process == "2"):
        amount = int(input("The amount you want to deposit:"))

        balance += amount
    elif (process == "3"):
        amount = int(input("The amount you want to withdraw:"))
        if (balance - amount < 0 ):
            print("Insufficient Balance.")
            print("Your balance {} is dollars".format(balance))
            continue
        balance -= amount

    else:
        print("Please enter a valid transaction.")
