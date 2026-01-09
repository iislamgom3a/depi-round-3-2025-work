class User:
    def __init__(self, name, age, gender, balance):
        self.name = name
        self.age = age 
        self.gender = gender
        self.balance = balance

    def show_data(self):
        print(f'name: {self.name}, age: {self.age}, gender: {self.gender}, balance, {self.balance} EGP')
