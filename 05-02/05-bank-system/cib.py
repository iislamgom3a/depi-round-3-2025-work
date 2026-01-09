from Bank_mod import bank


class CIB(bank.Bank):
    loan_amount = int()
    loan_duration = int()

    def loan_application(self, amount, duration):
        if amount > 1_000_000:
            print("Loan request exceeds QNB maximum limit of 1,000,000.")
        else:
            print(f"Loan of {amount} approved for duration: {duration} years.")
            self.loan_amount = amount
            self.loan_duration = duration

    def loan_info(self):
        print(
            f"Your loan is: {self.loan_amount} EGP ...for : {self.loan_duration} YEARS"
        )

    def info_loan_duration(self, end_date):
        print("-" * 10)
        print("End of duration is : ", end_date)
        print("-" * 10)
