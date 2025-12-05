from transaction import Income, Expense
from reports import ReportStrategy

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print("Transaction added successfully!")

    def edit_transaction(self, index, amount=None, category=None, date=None):
        try:
            t = self.transactions[index]
            if amount is not None:
                t._amount = amount
            if category is not None:
                t._category = category
            if date is not None:
                t._date = date
            print("Transaction updated successfully!")
        except IndexError:
            print("Invalid transaction index!")

    def delete_transaction(self, index):
        try:
            self.transactions.pop(index)
            print("Transaction deleted successfully!")
        except IndexError:
            print("Invalid transaction index!")

    def calculate_totals(self):
        total_income = sum(t._amount for t in self.transactions if isinstance(t, Income))
        total_expense = sum(t._amount for t in self.transactions if isinstance(t, Expense))
        balance = total_income - total_expense
        return {"income": total_income, "expense": total_expense, "balance": balance}

    def display_summary(self):
        totals = self.calculate_totals()
        print(f"Total Income: {totals['income']}")
        print(f"Total Expenses: {totals['expense']}")
        print(f"Balance: {totals['balance']}")

    def display_report(self, report_strategy: ReportStrategy):
        print(report_strategy.generate(self.transactions))
