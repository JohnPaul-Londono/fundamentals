class User:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawawl(self, amount):
        self.balance -= amount
        return self 

    def display_user_balance(self):
        return self.balance

    def transfer(from_user, to_user, amount):
        from_user.make_withdrawawl(amount)
        to_user.make_deposit(amount)

user1 = User("JonL", 500)
user2 = User("Kya", 2000 )
user3 = User("Bumi", 2500)

# print(user1.balance)
# print(user2.balance)
# print(user3.balance)

print(user1.balance)
user1.make_deposit(400).make_deposit(600).make_deposit(800).make_withdrawawl(400)
print(user1.balance)

print(user2.balance)
user2.make_deposit(700).make_deposit(1700).make_withdrawawl(600)
print(user2.balance)

print(user3.balance)
user3.make_deposit(4600).make_withdrawawl(800).make_withdrawawl(600).make_withdrawawl(400)
print(user2.balance)

# transfer
# print(user2.balance)
# print(user3.balance)
# User.transfer(user2, user3,500)
# print(user2.balance)
# print(user3.balance)