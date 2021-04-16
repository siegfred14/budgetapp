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


shop = Budget(500, 4000, 3000)
print(shop.cloth)
shop.menu()
