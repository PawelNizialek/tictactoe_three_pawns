"""
    Przechowuje planszę do gry.
"""
NUMBER_OF_BUTTONS = 9
NUMBER_OF_BUTTONS_TO_WIN = 3
COMPUTER_LOST = -1
COMPUTER_WON = 1
TIE = 0


class Board:
    """
        Plansza do gry.
        Sprawdzenie wygranej.
    """

    def __init__(self):
        self.board = [' '] * NUMBER_OF_BUTTONS
        self.computer_shape = 'O'
        self.player_shape = 'X'
        self.move = 0
        self.field_delete = 0
        self.game_run = 0
        self.pawns_limit_on_board = 0
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
        point = COMPUTER_WON
        for i in range(0, NUMBER_OF_BUTTONS_TO_WIN):
            if (self.board[i + 6] != " " and self.board[i] ==
                    self.board[i + 3] == self.board[i + 6]):
                if self.board[i] == shape_player:
                    point = COMPUTER_LOST
                return point
        point = COMPUTER_WON
        if self.board[4] != " " and (self.board[2] == self.board[4]
                                     == self.board[6] or (self.board[0]
                                                          == self.board[4] == self.board[8])):
            if self.board[4] == shape_player:
                point = COMPUTER_LOST
            return point
        for i in range(0, 7, 3):
            if (self.board[i + 2] != " " and self.board[i] == self.board[i + 1]
                    == self.board[i + 2]):
                if self.board[i] == shape_computer:
                    return COMPUTER_WON
                return COMPUTER_LOST
        for i in range(0, NUMBER_OF_BUTTONS):
            if self.board[i] != " ":
                count = count + 1
        if count == NUMBER_OF_BUTTONS:
            return TIE
