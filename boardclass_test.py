"""
Testy modułu boardclass
"""

import unittest

import boardclass


CIRCLE = "O"
CROSS = "X"
BLANK_FIELD = ' '
CHECKED_FIELDS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6), ]

TIE_FIELDS = [(0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7), (0, 1, 8),
              (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 2, 6), (0, 2, 7), (0, 2, 8),
              (0, 3, 1), (0, 3, 2), (0, 3, 4), (0, 3, 5), (0, 3, 7), (0, 3, 8),
              (0, 4, 1), (0, 4, 2), (0, 4, 3), (0, 4, 5), (0, 4, 6), (0, 4, 7),
              (0, 5, 1), (0, 5, 2), (0, 5, 3), (0, 5, 4), (0, 5, 6), (0, 5, 7),
              (0, 6, 1), (0, 6, 2), (0, 6, 4), (0, 6, 5), (0, 6, 7), (0, 6, 8),
              (0, 7, 1), (0, 7, 2), (0, 7, 4), (0, 7, 5), (0, 7, 6), (0, 1, 8),
              (0, 8, 1), (0, 8, 2), (0, 8, 3), (0, 8, 5), (0, 8, 6), (0, 8, 7),
              (4, 0, 2), (1, 8, 6), (1, 3, 7), (6, 1, 2), (4, 1, 8), (2, 3, 4), ]


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.test_board = boardclass.Board(CIRCLE, 0)

    def test_win(self):
        for field_list in CHECKED_FIELDS:
            board = [BLANK_FIELD] * 9
            for field in field_list:
                board[field] = CROSS
            self.test_board.board = board
            self.assertTrue(self.test_board.win_checker(CROSS, CIRCLE))

    def test_defeat(self):
        for field_list in CHECKED_FIELDS:
            board = [BLANK_FIELD] * 9
            for field in field_list:
                board[field] = CIRCLE
            self.test_board.board = board
            self.assertTrue(self.test_board.win_checker(CROSS, CIRCLE))

    def test_no_win(self):
        for field_list in TIE_FIELDS:
            board = [BLANK_FIELD] * 9
            for field in field_list:
                board[field] = CROSS
            self.test_board.board = board
            self.assertFalse(self.test_board.win_checker(CROSS, CIRCLE))


if __name__ == '__main__':
    unittest.main()
