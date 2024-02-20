from src.services.StudentService import StudentService


class Test:
    def __init__(self, repo):
        self.student_service = StudentService(repo)

    def test_random_values(self):
        assert len(self.student_service.get_all_students()) == 10

    def test_add(self):
        self.student_service.add_student(100, "Ion", 914, True)
        assert len(self.student_service.get_all_students()) == 11
        self.student_service.add_student(101, "Ana", 913, True)
        assert len(self.student_service.get_all_students()) == 12
        self.student_service.add_student(100, "Mateiut", 913, True)
        assert len(self.student_service.get_all_students()) == 12

    def test_filter(self):
        self.student_service.add_student(102, "George", 914, True)
        self.student_service.add_student(103, "Florica", 914, True)
        self.student_service.filter_students(914)
        assert len(self.student_service.get_all_students()) == 11

    def test_undo(self):
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_all_students()) == 14
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_all_students()) == 13
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_all_students()) == 12
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_all_students()) == 11
        self.student_service.undo_last_operation()
        assert len(self.student_service.get_all_students()) == 10

    def test_clear(self):
        self.student_service.clear_students()
        assert len(self.student_service.get_all_students()) == 0

    def test_all(self):
        self.test_random_values()


