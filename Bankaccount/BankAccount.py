class BankAccount:

    def __init__(self, account, balance, int_rate = 0.05) : 
        self.account = account
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        if(self.balance < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Account: {self.account}, Balance: {self.balance}")

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self

solo = BankAccount("John", 000)
joint = BankAccount("J & S", 2000) 



print(f"Account: {solo.account}, Balance:{solo.balance}")
solo.deposit(400).deposit(500).deposit(540).withdraw(320).yield_interest().display_account_info()



print(f"Account: {joint.account}, Balance: {joint.balance}")
joint.deposit(4500).deposit(550).withdraw(540).withdraw(320).withdraw(650).withdraw(20).yield_interest().display_account_info()



# solo.display_account_info()
# joint.display_account_info()
# print(solo.balance)