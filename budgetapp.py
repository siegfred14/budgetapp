class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.cloth = clothing
        self.entertain = entertainment

    # # creating a database for our budgets
    # budget_record = {
    #     "food": 0,
    #     "clothing": 0,
    #     "entertainment": 0
    # }
    #
    # # setting values for keys
    # set_food_budget = int(input("Enter Budget for food"))
    # set_clothing_budget = int(input("Enter Budget for Clothing"))
    # set_entertainment_budget = int(input("Enter Budget for Entertainment"))
    #
    # # updating database
    # budget_record["food"] += set_food_budget
    # budget_record["clothing"] += set_clothing_budget
    # budget_record["entertainment"] += set_entertainment_budget
    #
    # # Total budget calculated
    # total_budget = budget_record["food"] + budget_record["clothing"] + budget_record["entertainment"]
    # print(f"Your Total Budget is {total_budget}")
    #

#     item = {""}
#     balance = 0

    def menu(self):
        menu_choice = int(input("W E L C O M E ! \n Please pick an option \n 1.) Deposit \n 2.) Withdrawal \n 3.) "
                                "Check Category Balances \n 4.) Transfer \n"))

        if menu_choice == 1:
            self.deposit()
        elif menu_choice == 2:
            self.withdraw()
        elif menu_choice == 3:
            self.balance()
        elif menu_choice == 4:
            self.transfer()
        else:
            print("Wrong input, Try again")
            self.menu()

    def deposit(self):
        deposit_choice = int(input('''
                                    Which category would you like to deposit to? \n 
                                    1.) for food \n 
                                    2.) for clothing \n 
                                    3.) for entertainment
                                    4.) exit
                                    '''))
        deposit_amount = int(input("W E L C O M E ! \n How Much would you like to deposit? \n "))

        if deposit_choice == 1:
            self.food += deposit_amount
        elif deposit_choice == 2:
            self.cloth += deposit_amount
        elif deposit_choice == 3:
            self.entertain += deposit_amount
        elif deposit_choice == 4:
            self.menu()
        else:
            print("Wrong input, Try again")
            self.deposit()

    # def withdraw(self):
    #
    #     withdrawn = input("W E L C O M E ! \n How Much would you like to withdraw? \n")
    #     if balance >= withdrawn:
    #         balance -= withdrawn
    #         return balance
    #     else:
    #         print("insufficient funds!")
    def balance(self):
        print("Your Balances are...")
        print(f"Food --> {self.food} \n Clothing --> {self.cloth} \n Entertainment --> {self.entertain}")

    def transfer(self):
        transfer_from = input("Category to transfer from ... \n 1 for Food \n 2 for Cloth \n 3 for Entertainment \n")
        transfer_amount = int(input("Enter Amount to transfer"))
        transfer_to = int(input("Category to transfer To ... \n 1 for Food \n 2 for Cloth \n 3 for Entertainment \n"))

        if transfer_from == 1:
            self.food -= transfer_amount
            if transfer_to == 2:
                self.cloth += transfer_amount
            elif transfer_to == 3:
                self.entertain += transfer_amount
            else:
                self.transfer()
            print(f"You have Transferred {transfer_amount} successfully")

        elif transfer_from == 2:
            self.cloth -= transfer_amount
            if transfer_to == 1:
                self.food += transfer_amount
            elif transfer_to == 3:
                self.entertain += transfer_amount
            else:
                self.transfer()
            print(f"You have Transferred {transfer_amount} successfully")

        if transfer_from == 3:
            self.entertain -= transfer_amount
            if transfer_to == 2:
                self.cloth += transfer_amount
            elif transfer_to == 1:
                self.food += transfer_amount
            else:
                self.transfer()
            print(f"You have Transferred {transfer_amount} successfully")

        else:
            print("Wrong Input")
            self.menu()


shop = Budget(500, 4000, 3000)
print(shop.cloth)
shop.menu()
