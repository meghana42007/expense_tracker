# utils.py
# Helper functions for input validation

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_choice():
    print("\nChoose Storage Type:")
    print("1. JSON")
    print("2. CSV")
    choice = input("Enter choice: ")

    return "json" if choice == "1" else "csv"