class Bank:
    def __init__(self):
        self.accbal = 0

    def Deposit(self):
        amount = int(input("Enter Amount: "))
        if (amount < 100):
            print("Amount is less than minimum deposit (100).")
        elif (amount % 100 != 0):
            print("Deposit only multiples of 100.")
        elif (amount > 50000):
            print("Amount should be less than 50k.")
        else:
            self.accbal += amount
            print(f"{amount} Deposited Successfully!")

    def Withdraw(self):
        amount = int(input("Enter Amount: "))
        if (amount < 100):
            print("Amount is too low to Withdraw.")
        elif (amount % 100 != 0):
            print("Amount is not a multiple of 100.")
        elif (amount > self.accbal):
            print("Insufficient balance.")
        elif(self.accbal-amount < 500):
            print("minimum balance is 500")
        elif (amount >= 20000):
            print("Transaction limit exceeded. Cannot withdraw more than 20k.")
        else:
            self.accbal -= amount
            print(f"{amount} Withdrawn Successfully!")

    def BalInquery(self):
        print(f"Your current balance is: {self.accbal}")

    def validate(self, count=0):
        pin = int(input("Enter the pin: "))
        count += 1
        if (pin == 1212):
            self.view()
        else:
            if (count < 3):
                print("Incorrect Pin. Try again.")
                self.validate(count)
            else:
                print("Card is blocked.")

    def view(self):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Bal Inquery\n0. Exit")
            choose_option = int(input("Enter Your Option: "))

            if choose_option == 1:
                self.Deposit()
            elif choose_option == 2:
                self.Withdraw()
            elif choose_option == 3:
                self.BalInquery()
            elif choose_option == 0:
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid option. Please try again.")


obj = Bank()
obj.validate(0)
