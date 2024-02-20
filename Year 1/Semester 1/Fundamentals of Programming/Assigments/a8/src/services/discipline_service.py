from src.repository.repository import Repository
from src.domain.discipline import Discipline
from src.services.base_service import BaseService

import random

class DisciplineService(BaseService):
    def __init__(self):
        super().__init__(Discipline)

    def generate_random_values(self):
        list_of_disciplines = ["Environmental Science", "Neuroscience", "Cultural Anthropology", "Astrophysics",
                               "Medical Ethics", "Criminal Justice", "Digital Marketing", "Political Philosophy",
                               "Creative Writing", "Comparative Literature", "Human Nutrition", "Urban Planning",
                               "Sociolinguistics", "Artificial Intelligence Ethics", "Ecological Economics",
                               "Human Rights Law", "Marine Biology", "Psycholinguistics"]
        for i in range(14):
            discipline_id = random.randint(i * 10 + 1, (i + 1) * 10)
            discipline_name = list_of_disciplines[i]
            self.add_element(discipline_id, discipline_name)