from file_processor import FileProcessor
import csv

from student import Student


class CsvProcessor(FileProcessor):
    def read_file_to_get_student_list(self, file_path):
        with open(file_path, mode= 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                student = Student(
                    rollnumber = row['rollnumber'],
                    fullname=row['fullname'],
                    dob=row['dob']
                )
                print(f"{student.rollnumber} - {student.fullname}")
                self.student_list.append(student    )