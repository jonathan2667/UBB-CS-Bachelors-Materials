import random
from src.domain.student import Student
from src.repository.MemoryRepository import MemoryRepository

class StudentService:
    def __init__(self, repo):
        self._repo = repo
        self.generate_random_values()

    def generate_random_values(self):
        list_of_names = ["Alexandru", "Beatrice", "Cristian", "Diana", "Eduard", "Fiona", "Gabriel", "Hana", "Irina",
                         "Jovan", "Karina", "Liam", "Nadia", "Octavian", "Petra", "Radu", "Simona", "Tiberiu", "Tessa",
                         "Ursula", "Vladimir"]

        for i in range(10):
            unique_id = random.randint((i + 1) * 10 + 1, (i + 2) * 50)
            name = random.choice(list_of_names)
            group = random.randint(1, 100)
            self.add_student(unique_id, name, group, False)

    def clear_students(self):
        self._repo.erase_data()

    def add_student(self, id : int, name : str, group : int, appnd: bool):
        new_student = Student(id, name, group)
        self._repo.add_new_student(new_student, appnd)

    def filter_students(self, group):
        self._repo.filter_students_according_to_group(group)

    def get_all_students(self):
        return self._repo.get_list_with_all_students()

    def undo_last_operation(self):
        self._repo.undo_last_operation()