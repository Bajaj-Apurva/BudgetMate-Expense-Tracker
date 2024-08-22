import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        date = datetime.datetime.now()
        expense = {"date": date, "amount": amount, "category": category}
        self.expenses.append(expense)
        print("Your expenses have been added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses are recorded yet.")
        else:
            print("\n**** Expense Tracker ****")
            for expense in self.expenses:
                print(f"Date of expenditure: {expense['date'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Amount of expenses: ₹{expense['amount']:.2f}")
                print(f"Category: {expense['category']}")
                print("-" * 30)

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses are recorded yet.")
        else:
            categories = set(expense['category'] for expense in self.expenses)
            print("\n*** Spending Patterns ***")
            for category in categories:
                total_spent = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
                print(f"{category}: ₹{total_spent:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n*** Expense Tracker Application ***")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice here (1-4): ")

        if choice == "1":
            amount = float(input("Enter the amount of expense: "))
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, category)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_spending_patterns()

        elif choice == "4":
            print("Hope you spent wisely! ")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
