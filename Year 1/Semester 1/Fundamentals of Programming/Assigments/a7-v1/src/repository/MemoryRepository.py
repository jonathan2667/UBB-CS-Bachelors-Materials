from src.domain.student import Student

LAST_PERFORMED_OPERATION = 1
BEGINNING_OF_STACK = 0

class RepoException(Exception):
    pass

class MemoryRepository:
    def __init__(self):
        self._all_students_data = {}
        self._stack_of_all_operations_done_to_student_list = []

    def erase_data(self):
        self._all_students_data.clear()

    def add_new_student(self, new_student, student_not_already_added_to_list: bool):
        if new_student.id in self._all_students_data:
            return RepoException("Student already in!")

        self._all_students_data[new_student.id] = new_student
        if student_not_already_added_to_list == True:
            operation = [2, new_student]
            self._stack_of_all_operations_done_to_student_list.append(operation)

    def get_list_with_all_students(self):
        return list(self._all_students_data.values())

    def filter_students_according_to_group(self, group):
        operation = [1]
        filtered_dict = {}
        for student in self._all_students_data.values():
            if student.group != group:
                filtered_dict[student.id] = student
            else:
                operation.append(student)
        self._all_students_data = filtered_dict.copy()
        self._stack_of_all_operations_done_to_student_list.append(operation)

    def delete_student(self, existing_student: Student):
        del self._all_students_data[existing_student.id]

    def add_students(self, list_of_students):
        for new_students in list_of_students:
            self._all_students_data[new_students.id] = new_students

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
            self.add_students(operation[1:])

        else:
            self.delete_student(operation[LAST_PERFORMED_OPERATION])

