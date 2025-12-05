from transaction import Income, Expense

class ReportStrategy:
    def generate(self, transactions):
        pass

class SummaryReport(ReportStrategy):
    def generate(self, transactions):
        total_income = sum(t._amount for t in transactions if isinstance(t, Income))
        total_expense = sum(t._amount for t in transactions if isinstance(t, Expense))
        balance = total_income - total_expense
        return f"Total Income: {total_income}\nTotal Expenses: {total_expense}\nBalance: {balance}"
