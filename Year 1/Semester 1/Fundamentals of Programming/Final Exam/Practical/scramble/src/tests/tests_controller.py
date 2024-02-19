from unittest import TestCase

from src.controller.controller import Controller
from src.repository.repository import Repository


class TestController(TestCase):
    def setUp(self):
        self.repo = Repository()
        self.controller = Controller(self.repo)

    def test_return_all(self):
        all_sentences = self.controller.return_all()
        self.assertEqual(all_sentences, self.repo.get_all())

    def test_choose_sentence(self):
        sentence = self.controller.choose_sentence()
        self.assertIn(sentence, self.repo.get_all())

    def test_shuffle(self):
        sentence = "Dream without fear"
        shuffled_sentence = self.controller.shuffle(sentence)
        self.assertNotEqual(sentence, shuffled_sentence)

    def test_swap(self):
        sentence = "Dream without fear"
        shuffled_sentence = self.controller.shuffle(sentence)
        output = self.controller.swap(shuffled_sentence, 2, 1, 1, 1)
        self.assertNotEqual(shuffled_sentence, output)
        self.assertRaises(ValueError, self.controller.swap, shuffled_sentence, 0, 0, 0, 0)

    def tearDown(self) -> None:
        pass
