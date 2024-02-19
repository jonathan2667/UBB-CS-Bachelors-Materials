from unittest import TestCase

from src.controller.controller import Controller
from src.repository.repository import Repository


class TestController(TestCase):
    def setUp(self) -> None:
        self.repository = Repository()
        self.controller = Controller(self.repository)
        self.repository.add("Sentence 1")
        self.repository.add("Sentence 2")
        self.repository.add("Sentence 3")

    def test_add(self):
        length = len(self.controller.return_all())
        self.controller.add("Hello!")
        self.assertEqual(length + 1, len(self.repository.get_all()))

    def test_choose_random(self):
        sentence = self.controller.choose_sentence()
        self.assertTrue(sentence in self.controller.return_all())

    def tearDown(self) -> None:
        pass
