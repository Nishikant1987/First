import csv

# File to store expenses
EXPENSES_FILE = "expenses.csv"

# Function to load expenses from a file
def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Function to save expenses to a file
def save_expenses(expenses):
    with open(EXPENSES_FILE, "w", newline="") as file:
        fieldnames = ["Date", "Category", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# Add a new expense
def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Bills): ")
    try:
        amount = float(input("Enter the amount: "))
        expenses.append({"Date": date, "Category": category, "Amount": str(amount)})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please try again.")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses to show!")
    else:
        print("\n--- Expenses ---")
        for expense in expenses:
            print(f"Date: {expense['Date']}, Category: {expense['Category']}, Amount: ${expense['Amount']}")
        print("----------------")

# View total expenses by category
def view_total_by_category(expenses):
    totals = {}
    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])
        totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("No expenses to show!")
    else:
        print("\n--- Total Expenses by Category ---")
        for category, total in totals.items():
            print(f"{category}: ${total:.2f}")
        print("----------------------------------")

# Main function
def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses by Category")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total_by_category(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
