class User :
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, balance)


class BankAccount():
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawl(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print("Your balance is =", self.balance)


user1 = User("richie", "richie@gmail.com", 0.04, 5000)
user1.account.make_deposit(7500)
user1.account.make_withdrawl(2250)
user1.account.display_user_balance()

# print(user1.account.balance)