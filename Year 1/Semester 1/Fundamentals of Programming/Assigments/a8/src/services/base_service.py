from src.repository.repository import Repository
from src.domain.student import Student
from src.domain.discipline import Discipline

import random

class BaseService:
    def __init__(self, element_type):
        self._repo = Repository()
        self._element_type = element_type
        self.generate_random_values()

    def generate_random_values(self):
        raise NotImplementedError("Subclasses must implement the generate_random_values method")

    def check_if_element_is_valid(self, id):
        self._repo.check_if_not_present(id)

    def add_element(self, id, name):
        new_element = self._element_type(id, name)
        self._repo.add(new_element)

    def get_element_by_id(self, id):
        return self._repo.get_element_by_id(id)

    def get_all_elements(self):
        return self._repo.get_all()

    def get_all_element_ids(self):
        return self._repo.get_all_ids()

    def update_element(self, id, name):
        updated_element = self._element_type(id, name)
        self._repo.update(updated_element)

    def delete_element(self, id):
        self._repo.remove(id)

    def delete_all_elements(self):
        self._repo.delete_all()

    def search_element_based_on_id(self, id):
        return self._repo.search_by_id(id)

    def search_element_based_on_name(self, name):
        return self._repo.search_by_name(name)