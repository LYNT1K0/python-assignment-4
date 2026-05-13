import json


class ResultSaver:
    def __init__(self, result, output_file):
        self.result = result
        self.output_file = output_file

    def save_json(self):
        with open(self.output_file, "w", encoding="utf-8") as file:
            json.dump(self.result, file, indent=4)

        print(f"Result saved to {self.output_file}")