from unittest import TestCase

from src.repository.repository import Repository


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.repository = Repository()

    def test_add(self):
        length = len(self.repository.get_all())
        self.repository.add("Hello!")
        self.assertEqual(length + 1, len(self.repository.get_all()))
        self.assertRaises(ValueError, self.repository.add, "Hello!")

    def tearDown(self) -> None:
        pass
