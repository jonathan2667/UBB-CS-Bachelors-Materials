from src.domain.student import Student
from src.repository.MemoryRepository import MemoryRepository
from src.domain.grade import Grade

class TextFileRepository(MemoryRepository):
    def __init__(self, file_name):
        super(TextFileRepository, self).__init__()
        self._file_name = file_name
        self.load_file()

    def erase_data(self):
        super().delete_all()
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
            super().add(new_student)

    def _save_file(self):
        text_output_file = open(self._file_name, "wt")
        for student in self.get_all():
            student_string = str(student.id) + "," + student.name + "\n"
            text_output_file.write(student_string)

        for grade in self.get_all_grades():
            grade_string = str(grade.student_id) + "," + str(grade.discipline_id) + "," + str(grade.grade_value) + "\n"
            text_output_file.write(grade_string)
        text_output_file.close()

    def add_new_student(self, new_student):
        super().add(new_student)
        self._save_file()

    def add_new_grade(self, new_grade):
        super().add_grades(new_grade)
        self._save_file()

    def undo_last_operation(self):
        super().undo_last_operation()
        self._save_file()