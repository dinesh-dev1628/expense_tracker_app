from models import Expense
from storage import load_expenses, save_expenses

class ExpenseManager:
    def add_expense(self, amount, category, note=""):
        expenses = load_expenses()
        expense = Expense(amount, category, note)
        expenses.append(expense.to_dict())
        save_expenses(expenses)

    def get_all_expenses(self):
        return load_expenses()
