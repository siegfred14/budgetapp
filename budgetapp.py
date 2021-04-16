# A Budget class which instantiates objects based on different budget categories
class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.cloth = clothing
        self.entertain = entertainment

    # menu method - a user friendly dashboard for transactions on budget app
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

    # Deposit method - to add cash into a budget category
    def deposit(self):
        deposit_amount = int(input("W E L C O M E ! \n How Much would you like to deposit? \n "))
        deposit_choice = int(input('''
                                    Which category would you like to deposit to? \n 
                                    1.) for food \n 
                                    2.) for clothing \n 
                                    3.) for entertainment \n
                                    4.) exit \n
                                    '''))

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
        print("Transaction Successful!")
        self.balance()

    # withdraw method - to remove cash from a budget category
    def withdraw(self):
        withdrawal_amount = int(input("W E L C O M E ! \n How Much would you like to withdraw? \n "))
        withdrawal_source = int(input('''   
                                            Which category would you like to withdraw from? \n 
                                            1.) for food \n 
                                            2.) for clothing \n 
                                            3.) for entertainment \n
                                            4.) exit \n
                                            '''))

        if withdrawal_source == 1:
            self.food -= withdrawal_amount
        elif withdrawal_source == 2:
            self.cloth -= withdrawal_amount
        elif withdrawal_source == 3:
            self.entertain -= withdrawal_amount
        elif withdrawal_source == 4:
            self.menu()
        else:
            print("Wrong input, Try again")
            self.withdraw()
        self.balance()

    # balance method - to compute balances on all budget categories
    def balance(self):
        print("Your Balances are...")
        print(f"Food --> {self.food} \n Clothing --> {self.cloth} \n Entertainment --> {self.entertain}")

    # Transfer method - to transfer balance between budget categories
    def transfer(self):
        transfer_from = int(input("Category to transfer from ... \n 1 food \n 2 for Cloth \n 3 for Entertainment \n"))
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
            self.balance()

        elif transfer_from == 2:
            self.cloth -= transfer_amount
            if transfer_to == 1:
                self.food += transfer_amount
            elif transfer_to == 3:
                self.entertain += transfer_amount
            else:
                self.transfer()
            print(f"You have Transferred {transfer_amount} successfully")
            self.balance()

        elif transfer_from == 3:
            self.entertain -= transfer_amount
            if transfer_to == 2:
                self.cloth += transfer_amount
            elif transfer_to == 1:
                self.food += transfer_amount
            else:
                self.transfer()
            print(f"You have Transferred {transfer_amount} successfully")
            self.balance()

        else:
            print("Wrong Input")
            self.transfer()


# instantiating the class with amounts for categories food, cloth and entertainment
weekend_shopping = Budget(500, 4000, 3000)

weekend_shopping.menu()
