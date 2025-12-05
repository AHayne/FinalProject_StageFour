import csv
import os

class Transaction:
    def __init__(self, amount, category, date):
        self._amount = amount
        self._category = category
        self._date = date

    def display_transaction(self):
        return f"{self._date} | {self._category} | {self._amount}"

    def to_list(self, t_type):
        return [t_type, self._amount, self._category, self._date]

    @staticmethod
    def from_list(data):
        t_type, amount, category, date = data
        amount = float(amount)
        if t_type == "Income":
            return Income(amount, category, date)
        else:
            return Expense(amount, category, date)

class Income(Transaction):
    def display_transaction(self):
        return f"Income: {super().display_transaction()}"

class Expense(Transaction):
    def display_transaction(self):
        return f"Expense: {super().display_transaction()}"

class ReportStrategy:
    def generate(self, transactions):
        pass

class SummaryReport(ReportStrategy):
    def generate(self, transactions):
        total_income = sum(t._amount for t in transactions if isinstance(t, Income))
        total_expense = sum(t._amount for t in transactions if isinstance(t, Expense))
        balance = total_income - total_expense
        return f"Total Income: {total_income}\nTotal Expenses: {total_expense}\nBalance: {balance}"

class CategoryReport(ReportStrategy):
    def generate(self, transactions):
        category_totals = {}
        for t in transactions:
            category = t._category
            category_totals.setdefault(category, 0)
            if isinstance(t, Expense):
                category_totals[category] -= t._amount
            else:
                category_totals[category] += t._amount
        report_lines = ["Category Totals:"]
        for cat, total in category_totals.items():
            report_lines.append(f"{cat}: {total}")
        return "\n".join(report_lines)

class BudgetTracker:
    def __init__(self, filename="transactions.csv"):
        self.transactions = []
        self.filename = filename
        self.load_transactions()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print("Transaction added successfully!")
        self.save_transactions()

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
            self.save_transactions()
        except IndexError:
            print("Invalid transaction index!")

    def delete_transaction(self, index):
        try:
            self.transactions.pop(index)
            print("Transaction deleted successfully!")
            self.save_transactions()
        except IndexError:
            print("Invalid transaction index!")

    def display_report(self, report_strategy: ReportStrategy):
        print(report_strategy.generate(self.transactions))

    def save_transactions(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for t in self.transactions:
                t_type = "Income" if isinstance(t, Income) else "Expense"
                writer.writerow(t.to_list(t_type))

    def load_transactions(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    self.transactions.append(Transaction.from_list(row))

def main():
    tracker = BudgetTracker()
    
    while True:
        print("\n--- Personal Budget Tracker ---")
        print("0. View All Transactions")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. View Summary")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "0":
            if tracker.transactions:
                print("\nAll Transactions:")
                for i, t in enumerate(tracker.transactions):
                    print(f"{i}: {t.display_transaction()}")
            else:
                print("No transactions yet.")

        elif choice == "1":
            amount_input = input("Amount: ")
            if amount_input.replace('.', '', 1).isdigit():
                amount = float(amount_input)
                category = input("Category: ")
                date = input("Date (YYYY-MM-DD): ")
                tracker.add_transaction(Income(amount, category, date))
            else:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            amount_input = input("Amount: ")
            if amount_input.replace('.', '', 1).isdigit():
                amount = float(amount_input)
                category = input("Category: ")
                date = input("Date (YYYY-MM-DD): ")
                tracker.add_transaction(Expense(amount, category, date))
            else:
                print("Invalid amount. Please enter a number.")

        elif choice == "3":
            index_input = input("Transaction index to edit: ")
            if index_input.isdigit():
                index = int(index_input)
                if 0 <= index < len(tracker.transactions):
                    amount_input = input("New Amount (leave blank to keep): ")
                    category = input("New Category (leave blank to keep): ")
                    date = input("New Date (leave blank to keep): ")
                    tracker.edit_transaction(
                        index,
                        amount=float(amount_input) if amount_input.replace('.', '', 1).isdigit() else None,
                        category=category if category else None,
                        date=date if date else None
                    )
                else:
                    print("Invalid index. No transaction exists at that number.")
            else:
                print("Invalid input! Please enter a valid number.")

        elif choice == "4":
            index_input = input("Transaction index to delete: ")
            if index_input.isdigit():
                index = int(index_input)
                if 0 <= index < len(tracker.transactions):
                    tracker.delete_transaction(index)
                else:
                    print("Invalid index. No transaction exists at that number.")
            else:
                print("Invalid input! Please enter a valid number.")

        elif choice == "5":
            if tracker.transactions:
                print("\n--- Overall Summary ---")
                tracker.display_report(SummaryReport())
                print("\n--- Summary by Category ---")
                tracker.display_report(CategoryReport())
            else:
                print("No transactions yet to summarize.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
