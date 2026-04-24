class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount
        print(f"Income added: ${amount:.2f}")

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})
        print(f"Expense added: ${amount:.2f} for {category}")

    def total_expenses(self):
        return sum(exp["amount"] for exp in self.expenses)

    def get_balance(self):
        return self.income - self.total_expenses()

    def show_summary(self):
        print("\n--- Budget Summary ---")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.total_expenses():.2f}")
        print(f"Remaining Balance: ${self.get_balance():.2f}")

        print("\nExpenses by Category:")
        categories = {}
        for exp in self.expenses:
            categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

        for cat, amt in categories.items():
            print(f"{cat}: ${amt:.2f}")

    def saving_suggestions(self):
        print("\n--- Suggestions ---")
        categories = {}
        for exp in self.expenses:
            categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

        if not categories:
            print("No expenses yet. Start tracking to get suggestions.")
            return

        highest = max(categories, key=categories.get)
        print(f"You spend the most on '{highest}'. Try reducing this category.")

        if self.get_balance() < 0:
            print("⚠️ You are overspending! Consider cutting back on non-essential expenses.")
        else:
            print("Good job! You're staying within your budget.")

# --- App Loop ---
tracker = BudgetTracker()

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Get Suggestions")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        tracker.add_income(amount)

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (food, rent, entertainment, etc.): ")
        tracker.add_expense(amount, category)

    elif choice == "3":
        tracker.show_summary()

    elif choice == "4":
        tracker.saving_suggestions()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")