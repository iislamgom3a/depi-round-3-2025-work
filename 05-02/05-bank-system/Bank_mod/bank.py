from User_mod import user 

class Bank(user.User): 
    def __init__ (self, name, age, gender, balance):
        super().__init__(name, age, gender, balance)

    def deposit(self, amount: float): 
        print("transaction done successfully ")
        self.balance += amount 
    def withdraw(self, amount: float): 
        if amount > self.balance: 
            print('Your balance is less than the required amount!')
        else : 
            self.balance -= amount
            print("transaction done successfully ")
    def view_balance(self) : 
        print(f"Your current balance is : {self.balance} EGP")