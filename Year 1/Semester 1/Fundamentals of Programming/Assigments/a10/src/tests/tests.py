import unittest

from src.services.game import Game

class TestBoard(unittest.TestCase):
    def testDraw(self):
        game = Game()
        for column in range(3):
            for repeat in range(6):
                game.drop_piece(column)
        for column in range(4, 6):
            for repeat in range(6):
                game.drop_piece(column)
        game.drop_piece(6)
        for repeat in range(6):
            game.drop_piece(3)
        for repeat in range(5):
            game.drop_piece(6)
        self.assertEqual(game.is_draw(), True)

    def testWinVertical(self):
        game = Game()
        for repeat in range(4):
            game.drop_piece(0)
            game.drop_piece(1)
        self.assertEqual(game.winning_move(0), True)

    def testWinHorizontal(self):
        game = Game()
        for column in range(4):
            game.drop_piece(column)
            game.drop_piece(column)
        self.assertEqual(game.winning_move(0), True)

    def testDropPieceValid(self):
        game = Game()
        self.assertEqual(game.is_valid_column(0), True)
        for repeat in range(6):
            game.drop_piece(0)
        self.assertEqual(game.is_valid_column(0), False)

    def testDropPieceInvalid(self):
        game = Game()
        self.assertEqual(game.is_valid_column(7), False)
        self.assertEqual(game.is_valid_column(-1), False)

    def testIsValidColumn(self):
        game = Game()
        self.assertEqual(game.is_valid_column(0), True)
        self.assertEqual(game.is_valid_column(-1), False)
        self.assertEqual(game.is_valid_column(7), False)

    def testAll(self):
            self.testDraw()
            self.testWinVertical()
            self.testWinHorizontal()
            self.testDropPieceValid()
            self.testDropPieceInvalid()
            self.testIsValidColumn()