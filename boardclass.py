"""
    Przechowuje planszę do gry.
"""


class Board:
    """
        Plansza do gry.
        Sprawdzenie wygranej.
    """
    shape_tab = []
    button_list = []

    def __init__(self):
        self.board = [' ', " ", " ", " ", ' ', " ", " ", " ", ' ']
        self.computer_shape = 'O'
        self.player_shape = 'X'
        self.update = 0
        self.field_deleted = 0
        self.game_run = 0
        self.pawns_limit = 0
        self.level = 0


    def modify(self, place_number, shape):
        """
            Ustawienie pionka na planszy.
        """
        self.board[place_number] = shape

    def win_checker(self, shape_player, shape_computer):
        """
           Sprawdzenie czy podane ustwienie jest wygrywające.
           Zwraca 1 jeśli wygrana komputera.
           Zwraca -1 jeśli przegrana.
           Zwraca 0 jeśli remis.
        """
        count = 0
        point = 1
        for i in range(0, 3):
            if (self.board[i + 6] != " " and self.board[i] == self.board[i + 3]
                    and self.board[i] == self.board[i + 6]):
                if self.board[i] == shape_player:
                    point = -1
                return point
        point = 0
        if (self.board[4] != " " and self.board[2] == self.board[4]
                and self.board[4] == self.board[6]
                or (self.board[0] == self.board[4]
                    and self.board[4] != " " and self.board[4] == self.board[8])):
            if self.board[4] == shape_player:
                point = -1
            if self.board[4] == shape_computer:
                point = 1
            return point
        for i in range(0, 7, 3):
            if (self.board[i + 2] != " " and self.board[i] == self.board[i + 1]
                    and self.board[i] == self.board[i + 2]):
                if self.board[i] == shape_player:
                    return -1
                return 1
        for i in range(0, 9):
            if self.board[i] != " ":
                count = count + 1
        if count == 9:
            return point
        return None
