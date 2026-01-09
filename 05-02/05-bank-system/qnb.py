from Bank_mod import bank

class QNB(bank.Bank):
    loan_amount = int()
    loan_duration = int()
    def loan_application(self, amount, duration):
        if amount > 2_000_000:
            print("Loan request exceeds QNB maximum limit of 2,000,000.")
        else:
            print(f"Loan of {amount} approved for duration: {duration} years.")
            self.loan_amount = amount
            self.loan_duration = duration

    def loan_info(self):
        print(f"Your loan is: {self.loan_amount} EGP ...for : {self.loan_duration} YEARS") 