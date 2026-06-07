# expense_manager.py
# Core logic of expense tracker

from models import Expense
from storage import Storage

class ExpenseManager:
    def __init__(self, storage_type="json"):
        self.storage_type = storage_type
        file = "expenses.json" if storage_type == "json" else "expenses.csv"
        self.storage = Storage(file)
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if self.storage_type == "json":
            return self.storage.load_json()
        else:
            return self.storage.load_csv()

    def save_expenses(self):
        if self.storage_type == "json":
            self.storage.save_json(self.expenses)
        else:
            self.storage.save_csv(self.expenses)

    def add_expense(self, title, amount, category):
        exp = Expense(title, amount, category)
        self.expenses.append(exp.to_dict())
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\n--- All Expenses ---")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. {exp['date']} | {exp['title']} | {exp['category']} | ₹{exp['amount']}")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            self.save_expenses()
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index")

    def summary(self):
        total = sum(float(exp["amount"]) for exp in self.expenses)
        print("\n--- Summary ---")
        print(f"Total Expenses: ₹{total}")

        categories = {}
        for exp in self.expenses:
            cat = exp["category"]
            categories[cat] = categories.get(cat, 0) + float(exp["amount"])

        print("\nCategory Wise Spending:")
        for k, v in categories.items():
            print(f"{k}: ₹{v}")