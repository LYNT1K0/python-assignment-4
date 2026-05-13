class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = []
        high_performers = 0

        for student in self.students:
            try:
                gpa = float(student['GPA'])
                gpas.append(gpa)

                if gpa > 3.5:
                    high_performers += 1

            except (ValueError, KeyError):
                continue

        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_performers
        }

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)

        super().print_results()

        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        countries = {}

        for student in self.students:
            country = student.get("country", "Unknown")

            if country in countries:
                countries[country] += 1
            else:
                countries[country] = 1

        sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(countries),
            "top_3": sorted_countries[:3]
        }

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)

        super().print_results()

        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"