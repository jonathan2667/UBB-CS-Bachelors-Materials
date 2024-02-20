from src.repository.MemoryRepository import MemoryRepository
from src.domain.discipline import Discipline
from src.services.base_service import BaseService
from src.repository.repository import Repository
from src.domain.commandthatcanbecalled import *

import random
from jproperties import Properties

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

class DisciplineService:
    def __init__(self, repository, undo_service):
        if get_repository_name() == "Memory":
            self._repo = MemoryRepository()
        elif get_repository_name() == "Text":
            self._repo = repository("disciplines.txt")
        elif get_repository_name() == "Binary":
            self._repo = repository("disciplines.bin")
        self.UndoRedoService = undo_service
        self.generate_random_values()
    def generate_random_values(self):
        list_of_disciplines = ["Environmental Science", "Neuroscience", "Cultural Anthropology", "Astrophysics",
                               "Medical Ethics", "Criminal Justice", "Digital Marketing", "Political Philosophy",
                               "Creative Writing", "Comparative Literature", "Human Nutrition", "Urban Planning",
                               "Sociolinguistics", "Artificial Intelligence Ethics", "Ecological Economics",
                               "Human Rights Law", "Marine Biology", "Psycholinguistics"]
        for i in range(14):
            discipline_id = random.randint(i * 10 + 1, (i + 1) * 10)
            discipline_name = list_of_disciplines[i]
            self.add_discipline(discipline_id, discipline_name)

    def check_if_discipline_is_valid(self, id: int):
        self._repo.check_if_not_present(id)

    def add_discipline(self, id: int, name: str):
        new_discipline = Discipline(id, name)
        self._repo.add_new_student(new_discipline)
        UndoCommand = CommandThatCanBeCalled(self._repo.remove, (id))
        RedoCommand = CommandThatCanBeCalled(self._repo.add_new_student, new_discipline)
        UndoRedoCommand = [Operation(UndoCommand, RedoCommand)]
        self.UndoRedoService.register_operation(OperationThatCascades(UndoRedoCommand))

    def get_discipline_by_id(self, id: int):
        return self._repo.get_element_by_id(id)

    def get_all_disciplines(self):
        return self._repo.get_all()

    def get_all_discipline_ids(self):
        return self._repo.get_all_ids()

    def update_discipline(self, id: int, name: str):
        RedoCommand = CommandThatCanBeCalled(self._repo.update, (id, name))
        UndoCommand = CommandThatCanBeCalled(self._repo.update, (id, name))
        UndoRedoCommand = [Operation(UndoCommand, RedoCommand)]
        self.UndoRedoService.register_operation(OperationThatCascades(UndoRedoCommand))

        updated_discipline = Discipline(id, name)
        self._repo.update(updated_discipline)

    def delete_discipline(self, id: int):
        list_of_commands = []
        UndoCommand = CommandThatCanBeCalled(self._repo.add_new_student, (id, self.get_discipline_by_id(id).name))
        RedoCommand = CommandThatCanBeCalled(self._repo.remove, (id))
        OperationForUndoRedo = Operation(UndoCommand, RedoCommand)

        list_of_commands.append(OperationForUndoRedo)
        self._repo.remove(id)

        self._repo.delete_grades_based_on_discipline(id)
        self.UndoRedoService.register_operation(OperationThatCascades(list_of_commands))



    def delete_all_disciplines(self):
        self._repo.delete_all()

    def search_discipline_based_on_id(self, id: int):
        return self._repo.search_by_id(id)

    def search_discipline_based_on_name(self, name: str):
        return self._repo.search_by_name(name)