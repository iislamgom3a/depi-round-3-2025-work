import cib
import qnb

db = {
    "Islam": {
        "password": "iislamgom3a",
        "age": 21,
        "gender": "male",
        "balance": 10000,
        "bank": "QNB",
        "loan": [0, 0],
    },
    "mark": {
        "password": "mark3",
        "age": 21,
        "gender": "male",
        "balance": 100000,
        "bank": "CIB",
        "loan": [0, 0],
    },
    "manar": {
        "password": "manar#",
        "age": 21,
        "gender": "female",
        "balance": 100000,
        "bank": "QNB",
        "loan": [0, 0],
    },
    "mawada": {
        "password": "mawada#",
        "age": 21,
        "gender": "female",
        "balance": 1000000,
        "bank": "CIB",
        "loan": [0, 0],
    },
}

if __name__ == "__main__":
    print("Welcome to DEPI cash!")
    usr = input("Enter your name: ")

    if usr in db:
        password = input("Enter your password: ")
        if db[usr]["password"] == password:
            data = db[usr]
            if data["bank"] == "CIB":
                curr_user = cib.CIB(usr, data["age"], data["gender"], data["balance"])
            elif data["bank"] == "QNB":
                curr_user = qnb.QNB(usr, data["age"], data["gender"], data["balance"])
            else:
                print("Unsupported bank.")
                exit()

            print("Logged in!")

            while True:
                print("----------------------------------")
                print("1. Deposit\n2. Withdraw\n3. Show Data\n4. Show Balance")
                print("5. Take a Loan\n6. Loan info\n7.Exit")
                print("----------------------------------")
                try:
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if choice == 1:
                    amnt = float(input("Enter the amount: "))
                    curr_user.deposit(amnt)
                    data["balance"] += amnt
                elif choice == 2:
                    amnt = float(input("Enter the amount: "))
                    curr_user.withdraw(amnt)
                    data["balance"] -= amnt
                elif choice == 3:
                    curr_user.show_data()
                    print(f"Bank: {db[usr]['bank']}")
                elif choice == 4:
                    curr_user.view_balance()
                elif choice == 5:
                    amnt = float(input("Enter loan amount: "))
                    durr = int(input("Enter duration in years: "))
                    curr_user.loan_application(amnt, durr)
                    db[usr]["loan"] = amnt
                    db[usr]["loan"] = durr

                elif choice == 6:
                    curr_user.loan_info()
                elif choice == 7:
                    print("Logged out!")
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Wrong password.")
    else:
        print("We don't know you!")
