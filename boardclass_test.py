"""
Testy modułu boardclass
"""

import unittest

import boardclass

CHECKED_FIELDS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6), ]


class BoardTest(unittest.TestCase):
    """
    Testy klasy Board.
    """

    def setUp(self):
        self.board = boardclass.Board([" ", " ", " ", " ", " ", " ", " ", " ", " "])

    def test_win(self):
        """Test metody win_checker, która sprawdza czy ustawienie pionków jest wygrywajace."""
        for j in range(8):
            tab = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            for i in range(3):
                tab[CHECKED_FIELDS[j][i]] = "X"
            self.board = boardclass.Board(tab)
            self.assertTrue(self.board.win_checker("X", "O"))


if __name__ == '__main__':
    unittest.main()
