from src.repository.repository import Repository
from src.domain.grade import Grade
from src.repository.grade_repository import GradeRepository

import random
import statistics

STUDENT_ID = 0
DISCIPLINE_ID = 1

class GradeService():
    def __init__(self):
        self._repo = GradeRepository()
        self._statistics = {}

    def generate_random_grades(self, students, disciplines):
        for _ in range(50):
            new_student = random.choice(students)
            new_discipline = random.choice(disciplines)
            grade = random.uniform(2, 10)
            self.add_grade(new_discipline, new_student, grade)

    def check_if_grade_is_valid(self, grade):
        self._repo.check_if_input_is_valid(grade)

    def add_grade(self, discipline_id, student_id, grade_value):
        new_grade = Grade(discipline_id, student_id, grade_value)
        self._repo.add(new_grade)

    def get_all_grades(self):
        return self._repo.get_all()

    def delete_grades_based_on_discipline(self, discipline_id):
        self._repo.delete_grades_based_on_discipline(discipline_id)

    def delete_gades_based_on_student(self, student_id):
        self._repo.delete_grades_based_on_student(student_id)

    def process_data(self):
        for grade in self.get_all_grades():
            key = (grade.student_id, grade.discipline_id)
            if key not in self._statistics:
                self._statistics.update({key: []})
            self._statistics[key].append(grade.grade_value)

    def failing_students(self):
        self.process_data()
        failing_students = []

        for key in self._statistics:
            average = statistics.mean(self._statistics[key])
            if average < 5:
                failing_students.append([key, average])

        return failing_students

    def best_students(self):
        self.process_data()
        students_grades = {}
        best_students = {}

        for key in self._statistics:
            average = statistics.mean(self._statistics[key])
            if key[STUDENT_ID] not in students_grades:
                students_grades.update({key[STUDENT_ID]: []})
            students_grades[key[STUDENT_ID]].append(average)

        for key in students_grades:
            average = statistics.mean(students_grades[key])
            best_students[key] = average

        return dict(sorted(best_students.items(), key=lambda item: item[1], reverse=True))

    def descending_avg_disciplines(self):
        self.process_data()
        discipline_grades = {}
        descending_avg_disciplines = {}

        for key in self._statistics:
            average = statistics.mean(self._statistics[key])

            if key[DISCIPLINE_ID] not in discipline_grades:
                discipline_grades.update({key[DISCIPLINE_ID]: []})

            discipline_grades[key[DISCIPLINE_ID]].append(average)

        for key in discipline_grades:
            average = statistics.mean(discipline_grades[key])
            descending_avg_disciplines[key] = average

        return dict(sorted(descending_avg_disciplines.items(), key=lambda item: item[DISCIPLINE_ID], reverse=True))