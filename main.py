from csv_file_processor import CsvProcessor
from excel_file_processor import ExcelProcessor
from file_processor import FileProcessor


if __name__ == "__main__":
    file_processor: FileProcessor = None
    print("Please enter the student list file path:")
    file_path = input().strip()
    print(f"File path entered: {file_path}")
    if file_path.endswith('.csv'):
        file_processor = CsvProcessor()
    elif file_path.endswith('.xlsx'):
        file_processor = ExcelProcessor()
    else:
        print("Unsupported file type. Please provide a .csv or .xlsx file.")
        exit(1)

    file_processor.read_file_to_get_student_list(file_path)
    file_processor.print_student_list()            