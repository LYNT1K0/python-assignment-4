import os

OUTPUT_FOLDER = "output"


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if not os.path.exists(self.filename):
            print(f"Error: {self.filename} not found")
            return False

        print(f"File found: {self.filename}")
        return True

    def create_output_folder(self):
        print("Checking output folder...")

        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
            print(f"Output folder created: {OUTPUT_FOLDER}")
        else:
            print(f"Output folder already exists: {OUTPUT_FOLDER}")