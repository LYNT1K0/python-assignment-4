import csv


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")

        try:
            with open(self.filename, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)

            print(f"Loaded {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print("File not found")
            return []

    def preview(self, limit=5):
        print(f"First {limit} students:")
        print("-" * 30)

        for student in self.students[:limit]:
            print(student)

        print("-" * 30)