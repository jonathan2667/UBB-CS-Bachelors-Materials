import json
import os
from src.domain.student import Student
from src.repository.MemoryRepository import MemoryRepository


class JSONRepository(MemoryRepository):
    def __init__(self, file_name="students.json"):
        super(JSONRepository, self).__init__()
        self._file_name = file_name
        self._init_file()
        self._load_file()

    def reset_file(self):
        json_output_file = open(self._file_name, "w")
        json_output_file.write("{}")
        json_output_file.close()

    def erase_data(self):
        super().erase_data()
        self.reset_file()

    def _init_file(self):
        filesize = os.path.getsize(self._file_name)
        if filesize == 0:
            self.reset_file()

    def _load_file(self):
        students_json_format = {}
        try:
            json_input_file = open(self._file_name)
            students_json_format = json.load(json_input_file)
            json_input_file.close()
        except IOError:
            pass

        for student in students_json_format:
            new_student = Student(student["_student__student_id"], student["_student__student_name"],student["_student__student_group"])
            super().add_new_student(new_student, False)

    def _save_file(self):
        students_list = []
        json_output_file = open(self._file_name, "w")
        for students in self.get_list_with_all_students():
            students_list.append(students.__dict__)
        json.dump(students_list, json_output_file, indent = 1)
        json_output_file.close()

    def add_new_student(self, new_student: Student, student_not_already_added_to_list: bool):
        super().add_new_student(new_student, student_not_already_added_to_list)
        self._save_file()

    def filter_students_according_to_group(self, group: int):
        super().filter_students_according_to_group(group)
        self._save_file()

    def undo_last_operation(self):
        super().undo_last_operation()
        self._save_file()