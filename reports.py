from collections import defaultdict

def monthly_summary(expenses, month):
    summary = defaultdict(float)
    for exp in expenses:
        if exp["date"].startswith(month):
            summary[exp["category"]] += exp["amount"]
    return summary
