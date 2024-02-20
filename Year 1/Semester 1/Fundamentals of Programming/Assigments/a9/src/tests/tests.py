from src.repository.repository_exception import RepositoryException
from src.services.discipline_service import DisciplineService
from src.services.student_service import StudentService
from src.services.grade_service import GradeService

import unittest

class TestDisciplines(unittest.TestCase):
    def test_generate_random_values_disciplines(self):
        discipline_service = DisciplineService()
        self.assertEqual(len(discipline_service.get_all_elements()), 14)

    def test_add_discipline(self):
        id = 16437892578239
        name = "D1"
        discipline_service = DisciplineService()
        discipline_service.add_element(id, name)
        self.assertEqual(len(discipline_service.get_all_elements()), 15)

    def test_add_discipline_duplicate(self):
        id = 156243785623784
        name = "D1"
        discipline_service = DisciplineService()
        discipline_service.add_element(id, name)
        with self.assertRaises(RepositoryException): discipline_service.add_element(id, name)

    def test_update_discipline(self):
        discipline_service = DisciplineService()
        disciplines = discipline_service.get_all_elements()

        discipline_service.update_element(disciplines[0].id, "Discipline1")
        disciplines = discipline_service.get_all_elements()

        self.assertEqual(disciplines[0].name, "Discipline1")


class TestStudents(unittest.TestCase):
    def test_get_ids(self):
        student_service = StudentService()
        self.assertEqual(len(student_service.get_all_element_ids()), 20)

    def test_add_student_duplicate(self):
        id = 1
        name = "D1"
        student_service = StudentService()
        student_service.add_element(id, name)
        with self.assertRaises(RepositoryException): student_service.add_element(id, name)

    def test_update_student(self):
        student_service = StudentService()
        students = student_service.get_all_elements()

        student_service.update_element(students[0].id, "S1")
        students = student_service.get_all_elements()

        self.assertEqual(students[0].name, "S1")

    def test_update_student_not_found(self):
        student_service = StudentService()
        id = 12738621
        name = "S1"
        with self.assertRaises(RepositoryException): student_service.update_element(id, name)

    def test_update_student_not_found(self):
        student_service = StudentService()
        id = 12738621
        with self.assertRaises(RepositoryException): student_service.delete_element(id)

    def test_search_after_id(self):
        student_service = StudentService()
        student_service.delete_all_elements()
        student_service.add_element(1, "Matei")
        student_service.add_element(2, "Petru")
        student_service.add_element(3, "Pavel")
        student_service.add_element(10, "Andrei")
        student_service.add_element(13, "Ioan")
        student_service.add_element(15, "Iuda")
        student_service.add_element(27, "Toma")
        student_service.add_element(31, "Luca")
        student_service.add_element(38, "Iosif")
        student_service.add_element(1101, "Maria")

        studs = student_service.search_element_based_on_id(1)

        self.assertEqual(len(studs), 6)

if __name__ == '__main__':
    unittest.main()