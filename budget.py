class Budget:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, name, amount, category):
        self.expenses.append({
            'name': name,
            'amount': amount,
            'category': category
        })

    def cal_balance(self):
        total_expenses = sum(item['amount'] for item in self.expenses)
        balance = self.income - total_expenses
        return balance

    def display_summary(self):
        print("Income: ${:.2f}".format(self.income))
        print("Expenses:")
        for expense in self.expenses:
            print("- {} ({}) - ${:.2f}".format(expense['name'], expense['category'], expense['amount']))
        print("Balance: ${:.2f}".format(self.cal_balance()))

def main():
    budget = Budget()

    while True:
        print("\nBudgeting App")
        print("1. Add/enter Income")
        print("2. Add/enter Expense")
        print("3. Display Statement")
        print("4. End")

        choice = input("Enter your choice: ")

        if choice == "1":
            income = float(input("Enter income amount: $"))
            budget.add_income(income)
            print("Income added successfully!")

        elif choice == "2":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            budget.add_expense(name, amount, category)
            print("Expense added successfully!")

        elif choice == "3":
            budget.display_summary()

        elif choice == "4":
            print("Exiting the Budgeting App.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
