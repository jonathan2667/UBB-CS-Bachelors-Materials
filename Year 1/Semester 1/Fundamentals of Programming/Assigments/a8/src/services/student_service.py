from src.repository.repository import Repository
from src.domain.student import Student
from src.services.base_service import BaseService

import random

class StudentService(BaseService):
    def __init__(self):
        super().__init__(Student)

    def generate_random_values(self):
        names = ["Dorothea", "Jonathan", "Eleanor", "Benjamin", "Penelope", "Theodore", "Isabella", "Oliver",
                 "Abigail", "Sebastian", "Grace", "Alexander", "Charlotte", "Ethan", "Amelia", "Jackson",
                 "Sophia", "William", "Ava", "Henry"]
        for i in range(20):
            id = random.randint(i * 10, (i + 1) * 10)
            name = names[random.randint(0, len(names)) - 1]
            self.add_element(id, name)

