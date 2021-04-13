class Shopping:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.cloth = clothing
        self.entertain = entertainment

    # option = input("Enter food, clothing or entertainment")
    balance = 0
    def deposit(self):
        input("W E L C O M E ! \n How Much would you like to deposit? \n")


    def withdraw(self):
        balance = 0
        withdrawn = input("W E L C O M E ! \n How Much would you like to withdraw? \n")
        if balance >= withdrawn:
            balance -= withdrawn
            return balance
        else:
            print("insufficient funds!")
