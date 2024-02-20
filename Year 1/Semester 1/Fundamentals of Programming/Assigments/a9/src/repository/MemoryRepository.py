from src.repository.repository_exception import RepositoryException
from src.domain.student import Student

LAST_PERFORMED_OPERATION = 1
BEGINNING_OF_STACK = 0

class MemoryRepository:
    def __init__(self):
        self._data = {}
        self._data_grades = []
        self._stack_of_all_operations_done_to_student_list = []

    def check_if_present(self, id):
        if id in self._data:
            raise RepositoryException("It is already in!")

    def check_if_not_present(self, id):
        if id not in self._data:
            raise RepositoryException("It is not in!")

    def get_element_by_id(self, id):
        return self._data[id]

    def add(self, object):
        self.check_if_present(object.id)
        self._data[object.id] = object

    def add_grade(self, grade):
        self._data[grade.student_id].add_grade(grade)

    def remove(self, id):
        self.check_if_not_present(id)
        del self._data[id]

    def update(self, object):
        self.check_if_not_present(object.id)
        self._data[object.id] = object

    def search_by_id(self, id):
        object_list = []
        id = str(id)

        for object in self._data.values():
            object_id = str(object.id)
            if id in object_id:
                object_list.append(object)

        return object_list

    def search_by_name(self, name):
        object_list = []
        name = name.lower()

        for object in self._data.values():
            object_name = object.name.lower()
            if name in object_name:
                object_list.append(object)

        return object_list

    def get_all(self):
        return list(self._data.values())

    def get_all_ids(self):
        return list(self._data.keys())

    def delete_all(self):
        self._data.clear()

    def add_new_student(self, object):
        self.check_if_present(object.id)
        self._data[object.id] = object

    def undo_last_operation(self):
        """
        If the last performed operation was filter, we have deleted students, so we have to add them back
        If he last performed operation was add, we have added a student, so we have to erase it
        :return:
        """
        if len(self._stack_of_all_operations_done_to_student_list) == BEGINNING_OF_STACK:
            return
        operation = self._stack_of_all_operations_done_to_student_list[-1]
        self._stack_of_all_operations_done_to_student_list.pop()

        if operation[BEGINNING_OF_STACK] == LAST_PERFORMED_OPERATION:
            self.add(operation[1:])

        else:
            self.remove(operation[LAST_PERFORMED_OPERATION])

    def check_if_input_is_valid_grades(self, grade_value):
        if not (grade_value >= 0 and grade_value <= 10):
            raise RepositoryException("This grade is not valid!")

    def add_grades(self, grade):
        self.check_if_input_is_valid_grades(grade.grade_value)
        self._data_grades.append(grade)

    def get_all_grades(self):
        return self._data_grades

    def delete_grades_based_on_discipline(self, discipline_id):
        self._data_grades = [object for object in self._data_grades if object.discipline_id != discipline_id]

    def delete_grades_based_on_student(self, student_id):
        self._data_grades = [object for object in self._data_grades if object.student_id != student_id]

    def remove_grade(self, grade):
        self.check_if_input_is_valid_grades(grade.grade_value)
        self._data_grades.remove(grade)
    def add_new_grade(self, grade):
        self.check_if_input_is_valid_grades(grade.grade_value)
        self._data_grades.append(grade)