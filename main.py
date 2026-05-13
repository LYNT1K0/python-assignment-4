from analytics import FileManager
from analytics import DataLoader
from analytics import ResultSaver
from analytics import Report

from analytics.analyser import GpaAnalyser
from analytics.analyser import CountryAnalyser

INPUT_FILE = "students.csv"
OUTPUT_FILE = "output/result.json"


fm = FileManager(INPUT_FILE)

if fm.check_file():
    fm.create_output_folder()

    dl = DataLoader(INPUT_FILE)
    dl.load()
    dl.preview()

    analysers = [
        GpaAnalyser(dl.students),
        CountryAnalyser(dl.students[:10])
    ]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    for analyser in analysers:
        print(analyser)
        analyser.analyse()
        analyser.print_results()

    saver = ResultSaver(analysers[0].result, OUTPUT_FILE)
    report = Report(analysers[0], saver)
    report.generate()