class Shopping:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.cloth = clothing
        self.entertain = entertainment

    # option = input("Enter food, clothing or entertainment")

    item = {""}
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
    def balance(self):
        pass

    def transfer(self):
        transfer_from = input("Which Category would you like to transfer from? ... \n")
        transfer_amount = int(input("Enter Amount to transfer"))

        transfer_to = int(input("Which Category would you like to transfer to? ...\n"))

        if transfer_from == food:
            food = food - transfer_amount

        else:
            print("Wrong Input")


shop = Shopping("pilau", "jacket", "movie")
print(shop.cloth)
shop.deposit()
