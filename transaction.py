class Transaction:
    def __init__(self, amount, category, date):
        self._amount = amount
        self._category = category
        self._date = date

    def display_transaction(self):
        return f"{self._date} | {self._category} | {self._amount}"

class Income(Transaction):
    def display_transaction(self):
        return f"Income: {super().display_transaction()}"

class Expense(Transaction):
    def display_transaction(self):
        return f"Expense: {super().display_transaction()}"
