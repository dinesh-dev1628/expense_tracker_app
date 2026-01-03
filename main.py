from expense_manager import ExpenseManager
from reports import monthly_summary

manager = ExpenseManager()

while True:
    print("\n1. Add Expense")
    print("2. View Monthly Report")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        note = input("Note (optional): ")
        manager.add_expense(amount, category, note)
        print("Expense added ✅")

    elif choice == "2":
        month = input("Enter month (YYYY-MM): ")
        expenses = manager.get_all_expenses()
        summary = monthly_summary(expenses, month)
        print("\nMonthly Report:")
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")

    elif choice == "3":
        break
