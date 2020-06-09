"""
Testy modułu boardclass
"""

import unittest

import boardclass

CHECKED_FIELDS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6), ]


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.test_board = boardclass.Board()

    def test_win(self):
        for j in range(8):
            tab = [' ']*9
            for i in range(3):
                tab[CHECKED_FIELDS[j][i]] = "X"
            self.test_board.board = tab
            self.assertTrue(self.test_board.win_checker("X", "O"))

    def test_defeat(self):
        for j in range(8):
            tab = [' ']*9
            for i in range(3):
                tab[CHECKED_FIELDS[j][i]] = "O"
            self.test_board.board = tab
            self.assertTrue(self.test_board.win_checker("X", "O"))

    def test_no_win(self):
        for j in range(8):
            tab = [' ']*9
            for i in range(3):
                tab[CHECKED_FIELDS[j][i]] = " "
            self.test_board.board = tab
            self.assertIsNone(self.test_board.win_checker("X", "O"))


if __name__ == '__main__':
    unittest.main()
