from src.repository.MemoryRepository import MemoryRepository
from src.domain.student import Student
from src.services.base_service import BaseService
from src.repository.repository import Repository
from jproperties import Properties
from src.domain.commandthatcanbecalled import *

import random

def get_repository_name():
    configs_properties = Properties()

    with open('settings.properties', 'rb') as config_file:
        configs_properties.load(config_file)

    repository_string = configs_properties.get("REPO").data
    repository_name = ""

    if repository_string == "Memory":
        return repository_string
    elif repository_string == "Text":
        return repository_string
    elif repository_string == "Binary":
        return repository_string

    else:
        raise ValueError(f"Invalid repository type specified in settings.properties: {repository_string}")


class StudentService:
    def __init__(self, repository, undo_service):
        if get_repository_name() == "Memory":
            self._repo = MemoryRepository()
        elif get_repository_name() == "Text":
            self._repo = repository("students.txt")
        elif get_repository_name() == "Binary":
            self._repo = repository("students.bin")
        self.UndoRedoService = undo_service
        self.generate_random_values()

    def generate_random_values(self):
        names = ["Dorothea", "Jonathan", "Eleanor", "Benjamin", "Penelope", "Theodore", "Isabella", "Oliver",
                 "Abigail", "Sebastian", "Grace", "Alexander", "Charlotte", "Ethan", "Amelia", "Jackson",
                 "Sophia", "William", "Ava", "Henry"]

        for i in range(20):
            id = random.randint(i * 10 + 1, (i + 1) * 10)
            name = names[random.randint(0, len(names)) - 1]
            self.add_student(id, name)

    def check_if_student_is_valid(self, id: int):
        self._repo.check_if_not_present(id)

    def add_student(self, id: int, name: str):
        new_student = Student(id, name)
        self._repo.add_new_student(new_student)
        UndoCommand = CommandThatCanBeCalled(self._repo.remove, (id))
        RedoCommand = CommandThatCanBeCalled(self._repo.add_new_student, new_student)
        UndoRedoCommand = [Operation(UndoCommand, RedoCommand)]
        self.UndoRedoService.register_operation(OperationThatCascades(UndoRedoCommand))
    def get_student_by_id(self, id: int):
        return self._repo.get_element_by_id(id)

    def get_all_students(self):
        return self._repo.get_all()

    def get_all_student_ids(self):
        return self._repo.get_all_ids()

    def update_student(self, id: int, name: str):
        RedoCommand = CommandThatCanBeCalled(self._repo.update, *(Student(id, name),))
        UndoCommand = CommandThatCanBeCalled(self._repo.update, *(self.get_student_by_id(id),))

        UndoRedoCommand = [Operation(UndoCommand, RedoCommand)]
        self.UndoRedoService.register_operation(OperationThatCascades(UndoRedoCommand))

        updated_student = Student(id, name)
        self._repo.update(updated_student)

    def delete_student(self, id: int):
        list_of_commands = []
        UndoOperation  = CommandThatCanBeCalled(self._repo.add_new_student, (id, self.get_student_by_id(id).name))
        RedoOperation  = CommandThatCanBeCalled(self._repo.remove, id)
        OperationForRedoUndo = Operation(UndoOperation, RedoOperation)

        list_of_commands.append(OperationForRedoUndo)
        self._repo.remove(id)

        self._repo.delete_grades_based_on_student(id)
        # UndoOperation  = CommandThatCanBeCalled(self._repo.remove, (id))
        # RedoOperation  = CommandThatCanBeCalled(self._repo.add_new_student, (id, self.get_student_by_id(id).name))
        # OperationForRedoUndo = Operation(UndoOperation, RedoOperation)
        # list_of_commands.append(OperationForRedoUndo)

        self.UndoRedoService.register_operation(OperationThatCascades(list_of_commands))
    def delete_all_students(self):
        self._repo.delete_all()

    def search_student_based_on_id(self, id: int):
        return self._repo.search_by_id(id)

    def search_student_based_on_name(self, name: str):
        return self._repo.search_by_name(name)