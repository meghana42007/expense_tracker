# main.py
# Run this file to start the application

from expense_manager import ExpenseManager
from utils import get_float, get_choice

def main():
    storage_type = get_choice()
    manager = ExpenseManager(storage_type)

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            amount = get_float("Enter amount: ")
            category = input("Enter category: ")
            manager.add_expense(title, amount, category)

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            manager.view_expenses()
            idx = int(input("Enter index to delete: ")) - 1
            manager.delete_expense(idx)

        elif choice == "4":
            manager.summary()

        elif choice == "5":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()