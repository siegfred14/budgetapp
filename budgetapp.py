class Shopping:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.cloth = clothing
        self.entertain = entertainment

    # creating a database for our budgets
    budget_record = {
        "food": 0,
        "clothing": 0,
        "entertainment": 0
    }

    # setting values for keys
    set_food_budget = int(input("Enter Budget for food"))
    set_clothing_budget = int(input("Enter Budget for Clothing"))
    set_entertainment_budget = int(input("Enter Budget for Entertainment"))

    # updating database
    budget_record["food"] += set_food_budget
    budget_record["clothing"] += set_clothing_budget
    budget_record["food"] += set_entertainment_budget

    # Total budget calculated
    total_budget = budget_record["food"] + budget_record["clothing"] + budget_record["entertainment"]
    print(f"Your Total Budget is {total_budget}")

#
#     item = {""}
#     balance = 0
#     def deposit(self):
#         input("W E L C O M E ! \n How Much would you like to deposit? \n")
#
#
#     def withdraw(self):
#         balance = 0
#         withdrawn = input("W E L C O M E ! \n How Much would you like to withdraw? \n")
#         if balance >= withdrawn:
#             balance -= withdrawn
#             return balance
#         else:
#             print("insufficient funds!")
#     def balance(self):
#         pass
#
#     def transfer(self):
#         transfer_from = input("Which Category would you like to transfer from? ... \n")
#         transfer_amount = int(input("Enter Amount to transfer"))
#
#         transfer_to = int(input("Which Category would you like to transfer to? ...\n"))
#
#         # if transfer_from == food:
#         #     food = food - transfer_amount
#         #
#         # else:
#         #     print("Wrong Input")
#
#
# shop = Shopping("pilau", "jacket", "movie")
# print(shop.cloth)
# shop.deposit()
