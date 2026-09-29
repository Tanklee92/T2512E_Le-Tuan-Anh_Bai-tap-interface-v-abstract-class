from file_processor import FileProcessor
import openpyxl
from student import Student


class ExcelProcessor(FileProcessor):
    def read_file_to_get_student_list(self, file_path):
        workbook = openpyxl.load_workbook(file_path, data_only=True)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0] is None:
                continue

            student = Student(
                rollnumber=str(row[0]).strip(),
                fullname=str(row[1]).strip(), 
                dob=str(row[2]).strip()
            )

            print(f"{student.rollnumber} - {student.fullname}")
            self.student_list.append(student)