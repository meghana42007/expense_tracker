# models.py
# Defines the Expense data structure

from datetime import datetime

class Expense:
    def __init__(self, title, amount, category, date=None):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert object to dictionary for JSON/CSV storage"""
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }