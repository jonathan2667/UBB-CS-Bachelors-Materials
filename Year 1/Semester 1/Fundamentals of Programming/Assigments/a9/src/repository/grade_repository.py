from src.repository.repository_exception import RepositoryException

class GradeRepository:

    def __init__(self):
        self._data=  []

    def check_if_input_is_valid(self, grade_value):
        if not (grade_value >= 0 and grade_value <= 10):
            raise RepositoryException("This grade is not valid!")

    def add(self, grade):
        self.check_if_input_is_valid(grade.grade_value)
        self._data.append(grade)

    def get_all(self):
        return self._data

    def delete_grades_based_on_discipline(self, discipline_id):
        self._data = [object for object in self._data if object.discipline_id != discipline_id]

    def delete_grades_based_on_student(self, student_id):
        self._data = [object for object in self._data if object.student_id != student_id]