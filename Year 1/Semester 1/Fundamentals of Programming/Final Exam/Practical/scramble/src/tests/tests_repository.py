from unittest import TestCase

from src.repository.repository import Repository


class TestRepository(TestCase):
    def setUp(self) -> None:
        self.repository = Repository()

    def test_get_all(self):
        all_sentences = self.repository.get_all()
        self.assertEqual(all_sentences, ['Scramble',
                                         'Dream without fear',
                                         'The quick brown fox jumps over the lazy dog',
                                         'Brevity is beautiful',
                                         'Work hard dream big'])

    def test_add_existing_sentence(self):
        self.assertRaises(ValueError, self.repository.add, "Scramble")

    def test_load_data(self):
        expected_sentences = ['Scramble', 'Dream without fear', 'The quick brown fox jumps over the lazy dog',
                              'Brevity is beautiful', 'Work hard dream big']
        all_sentences = self.repository.get_all()
        self.assertEqual(all_sentences, expected_sentences)

    def tearDown(self):
        pass
