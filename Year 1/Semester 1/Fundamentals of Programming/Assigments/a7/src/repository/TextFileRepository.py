from src.domain.student import Student
from src.repository.MemoryRepository import MemoryRepository
import sys

class TextFileRepository(MemoryRepository):
    def __init__(self, file_name="students.txt"):
        super(TextFileRepository, self).__init__()
        self._file_name = file_name
        self.load_file()

    def erase_data(self):
        super().erase_data()
        open(self._file_name, "w").close()

    def load_file(self):
        lines_from_text_file = []
        try:
            test_file_input = open(self._file_name, "rt")
            lines_from_text_file = test_file_input.readlines()
            test_file_input.close()
        except IOError:
            pass

        for line in lines_from_text_file:
            current_line = line.split(',')
            new_student = Student(int(current_line[0].strip()), current_line[1].strip(), int(current_line[2].strip()))
            super().add_new_student(new_student, False)

    def _save_file(self):
        text_output_file = open(self._file_name, "wt")
        for student in self.get_list_with_all_students():
            student_string = str(student.id) + "," + student.name + "," + str(student.group) + "\n"
            text_output_file.write(student_string)
        text_output_file.close()

    def add_new_student(self, new_student: Student, student_not_already_added_to_list: bool):
        super().add_new_student(new_student, student_not_already_added_to_list)
        self._save_file()

    def filter_students_according_to_group(self, group: int):
        super().filter_students_according_to_group(group)
        self._save_file()

    def undo_last_operation(self):
        super().undo_last_operation()
        self._save_file()