from Bank_Account import BankAccount

class User:
    def __init__(self, name,):
        self.name = name
        # self.balance = balance
        self.account = {
            "solo": BankAccount(0),
            "joint": BankAccount(0)
        }

    # def make_deposit(self, amount):
    #     self.account.deposit(amount)
    #     return self

    # def make_withdrawawl(self, amount):
    #     self.account.withdraw(amount)
    #     return self 

    # def display_user_balance(self):
    #     self.account.display_account_info()
    #     return self

    def transfer(from_user, to_user, amount):
        from_user.make_withdrawawl(amount)
        to_user.make_deposit(amount)

user1 = User("JonL")
user2 = User("Kya")
user3 = User("Bumi")

print(user1.name)
user1.account["solo"].deposit(986).yield_interest().display_account_info()
user1.account["joint"].deposit(5436).yield_interest().display_account_info()

# print(user2.account.display_account_info)

# user2.make_deposit(500).interest_yield()
# user2.interest_yield()
# print(user2.account.balance)

# print(user1.balance)
# print(user2.balance)
# print(user3.balance)

# print(user1.balance)
# user1.make_deposit(400).make_deposit(600).make_deposit(800).make_withdrawawl(400)
# print(user1.balance)

# print(user2.balance)
# user2.make_deposit(700).make_deposit(1700).make_withdrawawl(600)
# print(user2.balance)

# print(user3.balance)
# user3.make_deposit(4600).make_withdrawawl(800).make_withdrawawl(600).make_withdrawawl(400)
# print(user2.balance)

# transfer
# print(user2.balance)
# print(user3.balance)
# User.transfer(user2, user3,500)
# print(user2.balance)
# print(user3.balance)