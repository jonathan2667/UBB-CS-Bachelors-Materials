import pickle
from src.domain.student import Student
from src.repository.MemoryRepository import MemoryRepository
from src.domain.grade import Grade

class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_name):
        super(BinaryFileRepository, self).__init__()
        self._file_name = file_name
        self._load_file()

    def erase_data(self):
        super().delete_all()
        open(self._file_name, "w").close()

    def _load_file(self):
        try:
            bin_input_file = open(self._file_name, 'rb')
            students_from_bin_file = pickle.load(bin_input_file)
        except EOFError:
            return
        for new_student in students_from_bin_file:
            super().add_new_student(new_student, False)
        bin_input_file.close()

    def _save_file(self):
        bin_out_file = open(self._file_name, "wb")
        pickle.dump(self.get_all(),  bin_out_file)
        pickle.dump(self.get_all_grades(), bin_out_file)
        bin_out_file.close()

    def add_new_student(self, new_student):
        super().add(new_student)
        self._save_file()

    def add_new_grade(self, new_grade):
        super().add_grades(new_grade)
        self._save_file()
    def undo_last_operation(self):
        super().undo_last_operation()
        self._save_file()