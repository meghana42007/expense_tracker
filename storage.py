# storage.py
# Handles saving/loading data in CSV or JSON

import csv
import json
import os

class Storage:
    def __init__(self, filename="expenses.json"):
        self.filename = filename

    # ---------- JSON HANDLING ----------
    def save_json(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_json(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    # ---------- CSV HANDLING ----------
    def save_csv(self, data):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "amount", "category", "date"])
            writer.writeheader()
            writer.writerows(data)

    def load_csv(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return list(csv.DictReader(f))